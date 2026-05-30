from pydantic import BaseModel, Field

from app.schemas.metrics import NormalisedMetricsTemplate


class GuidedMetricsRequest(BaseModel):
    project_name: str | None = None
    buying_context: str
    goals: list[str] = Field(default_factory=list)
    constraints: list[str] = Field(default_factory=list)
    must_have_requirements: list[str] = Field(default_factory=list)


class GuidedMetricsResponse(BaseModel):
    metrics_storage_path: str
    metrics_template: NormalisedMetricsTemplate
    raw_model_output: dict
