from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, File, Form, HTTPException, UploadFile, status

from app.schemas.upload import FileKind, UploadedFileResponse


router = APIRouter(prefix="/upload", tags=["upload"])

BASE_DIR = Path(__file__).resolve().parents[1]
UPLOAD_DIR = BASE_DIR / "storage" / "uploads"

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


@router.post("", response_model=list[UploadedFileResponse])
async def upload_files(
    kind: FileKind = Form(...),
    files: list[UploadFile] = File(...),
) -> list[UploadedFileResponse]:
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    uploaded: list[UploadedFileResponse] = []
    for file in files:
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

        uploaded.append(
            UploadedFileResponse(
                file_id=file_id,
                original_filename=_safe_filename(file.filename),
                stored_filename=stored_name,
                kind=kind,
                content_type=file.content_type,
                size_bytes=len(content),
                storage_path=str(stored_path),
            )
        )

    return uploaded
