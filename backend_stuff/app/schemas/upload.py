from enum import Enum

from pydantic import BaseModel

from app.schemas.metrics import NormalisedMetricsTemplate
from app.schemas.quotation import NormalisedQuotation


class FileKind(str, Enum):
    quotation = "quotation"
    metrics_template = "metrics_template"


class UploadedFileResponse(BaseModel):
    file_id: str
    original_filename: str
    stored_filename: str
    kind: FileKind
    content_type: str | None
    size_bytes: int
    storage_path: str


class UploadAndNormaliseResponse(BaseModel):
    file_id: str
    original_filename: str
    stored_filename: str
    kind: FileKind
    content_type: str | None
    size_bytes: int
    storage_path: str
    normalised_storage_path: str
    normalised: NormalisedQuotation | NormalisedMetricsTemplate
