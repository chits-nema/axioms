from enum import Enum

from pydantic import BaseModel, Field


class MetricDirection(str, Enum):
    higher_is_better = "higher_is_better"
    lower_is_better = "lower_is_better"


class ProcurementMetric(BaseModel):
    name: str
    weight: float = Field(ge=0)
    direction: MetricDirection
    description: str | None = None


class NormalisedMetricsTemplate(BaseModel):
    metrics: list[ProcurementMetric] = Field(default_factory=list)
