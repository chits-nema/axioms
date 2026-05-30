from typing import Any

from pydantic import BaseModel, Field

from app.schemas.metrics import MetricCategory


class DecisionCriterion(BaseModel):
    key: str
    category: MetricCategory
    label: str
    description: str | None = None
    score: int = Field(default=3, ge=1, le=5)


class RequirementsDiscoveryRequest(BaseModel):
    purchase: str
    organisation_context: str
    success_factors: list[str] = Field(default_factory=list)
    constraints: list[str] = Field(default_factory=list)
    normalised_quotations: list[dict[str, Any]] = Field(default_factory=list)


class RequirementsDiscoveryResult(BaseModel):
    criteria: list[DecisionCriterion] = Field(default_factory=list)


class RequirementsDiscoveryResponse(BaseModel):
    requirements_storage_path: str
    criteria: list[DecisionCriterion]
    raw_model_output: dict


class TradeoffQuestion(BaseModel):
    question_id: str
    left_key: str
    left_label: str
    right_key: str
    right_label: str
    prompt: str


class TradeoffQuestionRequest(BaseModel):
    criteria: list[DecisionCriterion]
    max_questions: int = Field(default=8, ge=1, le=20)


class TradeoffQuestionResponse(BaseModel):
    questions: list[TradeoffQuestion]


class TradeoffAnswer(BaseModel):
    question_id: str
    selected_key: str


class WeightingHandoffRequest(BaseModel):
    criteria: list[DecisionCriterion]
    tradeoff_answers: list[TradeoffAnswer]


class WeightingHandoffResponse(BaseModel):
    status: str
    weighting_input_storage_path: str
    criteria: list[DecisionCriterion]
    tradeoff_answers: list[TradeoffAnswer]
