import json
from typing import Any

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

from app.catalogue_to_context.retriever import get_vendor_context
from app.services.normaliser import (
    NormalisationError,
    call_llm_json,
    generate_metrics_from_context,
)


router = APIRouter(prefix="/catalog", tags=["catalog"])


class PurchaseRequest(BaseModel):
    product: str = Field(..., description="The product to evaluate.")
    metrics: list[str] = Field(default_factory=list, description="Optional evaluation metrics.")
    metric_weights: dict[str, float] = Field(default_factory=dict, description="Optional metric weights.")
    category: str | None = Field(default=None, description="Optional catalogue category filter.")
    vendors: list[str] = Field(default_factory=list, description="Optional vendor filter.")


class VendorScore(BaseModel):
    vendor_name: str
    scores: dict[str, int]
    final_weighted_score: float
    justification: str


class FinalRecommendation(BaseModel):
    rankings: list[VendorScore]
    summary: str


@router.post("/evaluate", response_model=dict[str, Any])
def evaluate_catalog_purchase(request: PurchaseRequest) -> dict[str, Any]:
    metrics = request.metrics
    generated_metrics_template = None

    if not metrics:
        metrics, generated_metrics_template = _generate_metrics_for_catalog(request)

    vendor_data = get_vendor_context(
        product=request.product,
        metrics=metrics,
        category=request.category,
        vendors=request.vendors or None,
    )

    if not vendor_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No relevant vendor documents found in the catalogue.",
        )

    context = "\n\n".join(
        f"### VENDOR: {vendor} ###\n{snippets}" for vendor, snippets in vendor_data.items()
    )
    try:
        payload, _raw_output = call_llm_json(
            _evaluation_prompt(request.product, metrics, request.metric_weights, context)
        )
    except NormalisationError as exc:
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=str(exc)) from exc

    try:
        recommendation = FinalRecommendation.model_validate(payload)
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"The model returned catalogue evaluation JSON, but it did not match the schema: {exc}",
        ) from exc

    return {
        "status": "success",
        "evaluated_product": request.product,
        "metrics_used": metrics,
        "generated_metrics_template": generated_metrics_template,
        "evaluation_results": recommendation.model_dump(mode="json"),
    }


def _generate_metrics_for_catalog(request: PurchaseRequest) -> tuple[list[str], dict[str, Any]]:
    try:
        template, _raw = generate_metrics_from_context(
            {
                "project_name": request.product,
                "buying_context": f"Evaluate catalogue vendors for {request.product}.",
                "goals": [f"Select the strongest vendor for {request.product}."],
                "constraints": [],
                "must_have_requirements": [],
                "category": request.category,
                "vendors": request.vendors,
            }
        )
    except NormalisationError as exc:
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=str(exc)) from exc

    metrics = [metric.name for metric in template.metrics]
    if not metrics:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="The metrics service did not return any catalogue metrics.",
        )

    return metrics, template.model_dump(mode="json")


def _evaluation_prompt(
    product: str,
    metrics: list[str],
    metric_weights: dict[str, float],
    context: str,
) -> str:
    weights = metric_weights or {metric: 1 for metric in metrics}
    return f"""
You are an impartial corporate purchasing agent.

Evaluate vendors for this product: {product}

Use only the verified facts from the vendor catalogue context. Do not invent facts, features, prices, or figures.

Metrics:
{json.dumps(metrics, indent=2)}

Metric weights:
{json.dumps(weights, indent=2)}

Return only valid JSON with this exact shape:
{{
  "rankings": [
    {{
      "vendor_name": "string",
      "scores": {{"metric name": 1}},
      "final_weighted_score": 0.0,
      "justification": "one sentence based on catalogue evidence"
    }}
  ],
  "summary": "short executive summary"
}}

Rules:
- Score every vendor from 1 to 10 for every metric.
- Calculate final_weighted_score using the metric weights.
- Sort rankings from highest final_weighted_score to lowest.
- Return JSON only, with no markdown or prose outside the JSON.

Vendor catalogue context:
{context}
""".strip()
