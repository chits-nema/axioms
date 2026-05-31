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
from app.weighted_metrics.matrix_calc import build_comparison_matrix
from app.weighted_metrics.llm_scorer import recommend_vendor

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
    
    vendors = [{"name": vendor, "description": snippets} for vendor, snippets in vendor_data.items()]
    criteria = [{"key": m, "label": m, "category": "functional", "description": "", "score": request.metric_weights.get(m, 3)} for m in metrics]

    try: 
        matrix = build_comparison_matrix(
            vendors=vendors,
            criteria=criteria,
            quotations=[],
            tradeoff_answers=[]
        )
    except Exception as exc: 
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=str(exc)) from exc
    
    evaluation_results = matrix.reset_index().to_dict(orient="records")
    recommendation = recommend_vendor(evaluation_results,criteria)
    return {
        "status": "success", 
        "evaluated_product": request.product,
        "metrics_used": metrics,
        "generated_metrics_template": generated_metrics_template,
        "evaluation_results": evaluation_results,
        "recommendation": recommendation
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