from enum import Enum

from pydantic import BaseModel, Field


class MetricDirection(str, Enum):
    higher_is_better = "higher_is_better"
    lower_is_better = "lower_is_better"


class MetricCategory(str, Enum):
    functional = "functional"
    financial = "financial"
    risks = "risks"
    strategic = "strategic"


class ProcurementMetric(BaseModel):
    name: str
    weight: float = Field(ge=0)
    direction: MetricDirection
    description: str | None = None
    category: MetricCategory | None = None
    score: int | None = Field(default=None, ge=1, le=5)


class MetricSubcategory(BaseModel):
    name: str
    score: int = Field(ge=1, le=5)
    direction: MetricDirection | None = None
    description: str | None = None
    weight: float | None = Field(default=None, ge=0)


class MetricCategoryGroup(BaseModel):
    category: MetricCategory
    category_weight: float | None = Field(default=None, ge=0)
    subcategories: dict[str, MetricSubcategory] = Field(default_factory=dict)


class NormalisedMetricsTemplate(BaseModel):
    categories: list[MetricCategoryGroup] = Field(default_factory=list)
    metrics: list[ProcurementMetric] = Field(default_factory=list)
