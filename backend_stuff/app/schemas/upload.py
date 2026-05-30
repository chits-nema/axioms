from enum import Enum

from pydantic import BaseModel


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
