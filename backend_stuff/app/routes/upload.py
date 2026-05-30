import json
from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, File, Form, HTTPException, UploadFile, status

from app.schemas.upload import FileKind, UploadAndNormaliseResponse, UploadedFileResponse
from app.services.file_parser import ParserError, parse_file
from app.services.normaliser import NormalisationError, normalise_document


router = APIRouter(prefix="/upload", tags=["upload"])

BASE_DIR = Path(__file__).resolve().parents[1]
UPLOAD_DIR = BASE_DIR / "storage" / "uploads"
NORMALISED_DIR = BASE_DIR / "storage" / "normalised"

ALLOWED_EXTENSIONS = {".pdf"}


def _safe_filename(filename: str) -> str:
    return Path(filename).name.replace(" ", "_")


def _validate_file(file: UploadFile) -> str:
    if not file.filename:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Uploaded file must have a filename.",
        )

    extension = Path(file.filename).suffix.lower()
    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail=f"Unsupported file type '{extension}'. Only PDF files are supported.",
        )

    return extension


async def _store_uploaded_file(file: UploadFile, kind: FileKind) -> UploadedFileResponse:
    extension = _validate_file(file)
    file_id = str(uuid4())
    stored_name = f"{file_id}{extension}"
    stored_path = UPLOAD_DIR / stored_name

    content = await file.read()
    if not content:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"{file.filename} is empty.",
        )

    stored_path.write_bytes(content)

    return UploadedFileResponse(
        file_id=file_id,
        original_filename=_safe_filename(file.filename),
        stored_filename=stored_name,
        kind=kind,
        content_type=file.content_type,
        size_bytes=len(content),
        storage_path=str(stored_path),
    )


def _store_normalised_json(
    upload: UploadedFileResponse,
    normalised: object,
    raw_model_output: dict,
) -> Path:
    NORMALISED_DIR.mkdir(parents=True, exist_ok=True)
    output_path = NORMALISED_DIR / f"{upload.file_id}_{upload.kind.value}.json"
    payload = {
        "file_id": upload.file_id,
        "kind": upload.kind.value,
        "source_pdf": upload.storage_path,
        "normalised": normalised.model_dump(mode="json"),
        "raw_model_output": raw_model_output,
    }
    output_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return output_path


@router.post("", response_model=list[UploadedFileResponse])
async def upload_files(
    kind: FileKind = Form(...),
    files: list[UploadFile] = File(...),
) -> list[UploadedFileResponse]:
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    uploaded: list[UploadedFileResponse] = []
    for file in files:
        uploaded.append(await _store_uploaded_file(file, kind))

    return uploaded


@router.post("/normalise", response_model=list[UploadAndNormaliseResponse])
async def upload_and_normalise_files(
    kind: FileKind = Form(...),
    files: list[UploadFile] = File(...),
) -> list[UploadAndNormaliseResponse]:
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    responses: list[UploadAndNormaliseResponse] = []
    for file in files:
        upload = await _store_uploaded_file(file, kind)

        try:
            parsed = parse_file(Path(upload.storage_path))
            normalised, raw_output = normalise_document(kind, parsed)
        except ParserError as exc:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=str(exc),
            ) from exc
        except NormalisationError as exc:
            raise HTTPException(
                status_code=status.HTTP_502_BAD_GATEWAY,
                detail=str(exc),
            ) from exc

        normalised_path = _store_normalised_json(upload, normalised, raw_output)
        responses.append(
            UploadAndNormaliseResponse(
                **upload.model_dump(),
                normalised_storage_path=str(normalised_path),
                normalised=normalised,
            )
        )

    return responses
