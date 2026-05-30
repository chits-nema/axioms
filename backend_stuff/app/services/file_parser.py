from __future__ import annotations

import io
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field


class ParserError(Exception):
    pass


class ParsedPage(BaseModel):
    page_number: int
    text: str


class ParsedTable(BaseModel):
    label: str
    rows: list[dict[str, Any]]


class ParsedDocument(BaseModel):
    filename: str
    extension: str
    text: str
    pages: list[ParsedPage] = Field(default_factory=list)
    tables: list[ParsedTable] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)


def parse_file(path: Path) -> ParsedDocument:
    extension = path.suffix.lower()

    if extension == ".pdf":
        return _parse_pdf(path)

    raise ParserError(f"Unsupported file type: {extension}. Only PDF files are supported.")


def _parse_pdf(path: Path) -> ParsedDocument:
    try:
        import fitz
    except ImportError as exc:
        raise ParserError("PDF parsing needs pymupdf. Install backend requirements.") from exc

    doc = fitz.open(path)
    pages: list[ParsedPage] = []
    warnings: list[str] = []

    for index, page in enumerate(doc, start=1):
        text = page.get_text("text").strip()
        if not text:
            text = _ocr_pdf_page(page)
            if text:
                warnings.append(f"Page {index} needed OCR because no embedded text was found.")
        pages.append(ParsedPage(page_number=index, text=text))

    combined_text = "\n\n".join(page.text for page in pages if page.text).strip()
    if not combined_text:
        warnings.append(
            "No text could be extracted. This is likely a scanned PDF; configure OCR or use a vision model."
        )

    return ParsedDocument(
        filename=path.name,
        extension=path.suffix.lower(),
        text=combined_text,
        pages=pages,
        warnings=warnings,
    )


def _ocr_pdf_page(page: Any) -> str:
    try:
        import pytesseract
        from PIL import Image
    except ImportError:
        return ""

    pixmap = page.get_pixmap(dpi=220)
    image = Image.open(io.BytesIO(pixmap.tobytes("png")))
    return pytesseract.image_to_string(image).strip()

