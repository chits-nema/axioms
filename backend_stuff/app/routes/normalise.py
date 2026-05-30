from pathlib import Path

from fastapi import APIRouter, HTTPException, status

from app.schemas.normalise import ExtractRequest, ExtractResponse, NormaliseRequest, NormaliseResponse
from app.services.file_parser import ParserError, parse_file
from app.services.normaliser import NormalisationError, build_normalisation_prompt, normalise_document


router = APIRouter(prefix="/normalise", tags=["normalise"])

BASE_DIR = Path(__file__).resolve().parents[1]
UPLOAD_DIR = (BASE_DIR / "storage" / "uploads").resolve()


def _resolve_uploaded_path(storage_path: str) -> Path:
    path = Path(storage_path)
    if not path.is_absolute():
        path = (UPLOAD_DIR / path).resolve()
    else:
        path = path.resolve()

    if UPLOAD_DIR not in path.parents:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only files inside app/storage/uploads can be normalised.",
        )

    if not path.exists():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"File does not exist: {path}",
        )

    return path


@router.post("/extract", response_model=ExtractResponse)
def extract_file(request: ExtractRequest) -> ExtractResponse:
    path = _resolve_uploaded_path(request.storage_path)

    try:
        parsed = parse_file(path)
    except ParserError as exc:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(exc),
        ) from exc

    return ExtractResponse(
        file_id=request.file_id,
        kind=request.kind,
        parsed=parsed,
        normalisation_prompt=build_normalisation_prompt(request.kind, parsed),
    )


@router.post("", response_model=NormaliseResponse)
def normalise_file(request: NormaliseRequest) -> NormaliseResponse:
    path = _resolve_uploaded_path(request.storage_path)

    try:
        parsed = parse_file(path)
        normalised, raw_output = normalise_document(request.kind, parsed)
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

    return NormaliseResponse(
        file_id=request.file_id,
        kind=request.kind,
        parsed=parsed,
        normalised=normalised,
        raw_model_output=raw_output,
    )
