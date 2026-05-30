import json
from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, HTTPException, status

from app.schemas.metrics_builder import GuidedMetricsRequest, GuidedMetricsResponse
from app.services.normaliser import NormalisationError, generate_metrics_from_context


router = APIRouter(prefix="/metrics", tags=["metrics"])

BASE_DIR = Path(__file__).resolve().parents[1]
NORMALISED_DIR = (BASE_DIR / "storage" / "normalised").resolve()


@router.post("/guide", response_model=GuidedMetricsResponse)
def guide_metrics(request: GuidedMetricsRequest) -> GuidedMetricsResponse:
    try:
        metrics_template, raw_model_output = generate_metrics_from_context(request.model_dump())
    except NormalisationError as exc:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=str(exc),
        ) from exc

    NORMALISED_DIR.mkdir(parents=True, exist_ok=True)
    output_path = NORMALISED_DIR / f"{uuid4()}_metrics_template.json"
    payload = {
        "kind": "metrics_template",
        "source": "guided_llm",
        "input": request.model_dump(mode="json"),
        "normalised": metrics_template.model_dump(mode="json"),
        "raw_model_output": raw_model_output,
    }
    output_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    return GuidedMetricsResponse(
        metrics_storage_path=str(output_path),
        metrics_template=metrics_template,
        raw_model_output=raw_model_output,
    )
