from pydantic import BaseModel

from app.schemas.metrics import NormalisedMetricsTemplate
from app.schemas.quotation import NormalisedQuotation
from app.schemas.upload import FileKind
from app.services.file_parser import ParsedDocument


class ExtractRequest(BaseModel):
    file_id: str
    storage_path: str
    kind: FileKind


class ExtractResponse(BaseModel):
    file_id: str
    kind: FileKind
    parsed: ParsedDocument
    normalisation_prompt: str


class NormaliseRequest(BaseModel):
    file_id: str
    storage_path: str
    kind: FileKind


class NormaliseResponse(BaseModel):
    file_id: str
    kind: FileKind
    parsed: ParsedDocument
    normalised: NormalisedQuotation | NormalisedMetricsTemplate
    raw_model_output: dict
