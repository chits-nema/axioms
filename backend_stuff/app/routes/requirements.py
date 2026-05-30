import json
from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, HTTPException, status

from app.schemas.requirements import (
    RequirementsDiscoveryRequest,
    RequirementsDiscoveryResponse,
    TradeoffQuestion,
    TradeoffQuestionRequest,
    TradeoffQuestionResponse,
    WeightingHandoffRequest,
    WeightingHandoffResponse,
)
from app.services.normaliser import NormalisationError, generate_requirements_criteria


router = APIRouter(prefix="/requirements", tags=["requirements"])

BASE_DIR = Path(__file__).resolve().parents[1]
REQUIREMENTS_DIR = (BASE_DIR / "storage" / "requirements").resolve()


@router.post("/discover", response_model=RequirementsDiscoveryResponse)
def discover_requirements(request: RequirementsDiscoveryRequest) -> RequirementsDiscoveryResponse:
    try:
        result, raw_model_output = generate_requirements_criteria(request.model_dump())
    except NormalisationError as exc:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=str(exc),
        ) from exc

    REQUIREMENTS_DIR.mkdir(parents=True, exist_ok=True)
    output_path = REQUIREMENTS_DIR / f"{uuid4()}_criteria.json"
    payload = {
        "source": "requirements_discovery",
        "input": request.model_dump(mode="json"),
        "criteria": [criterion.model_dump(mode="json") for criterion in result.criteria],
        "raw_model_output": raw_model_output,
    }
    output_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    return RequirementsDiscoveryResponse(
        requirements_storage_path=str(output_path),
        criteria=result.criteria,
        raw_model_output=raw_model_output,
    )


@router.post("/tradeoffs", response_model=TradeoffQuestionResponse)
def create_tradeoff_questions(request: TradeoffQuestionRequest) -> TradeoffQuestionResponse:
    questions: list[TradeoffQuestion] = []
    criteria = request.criteria

    for index, left in enumerate(criteria):
        if len(questions) >= request.max_questions:
            break

        right = _find_next_different_category(criteria, index)
        if right is None:
            continue

        questions.append(
            TradeoffQuestion(
                question_id=f"tradeoff_{len(questions) + 1}",
                left_key=left.key,
                left_label=left.label,
                right_key=right.key,
                right_label=right.label,
                prompt="Which matters more for this purchase?",
            )
        )

    return TradeoffQuestionResponse(questions=questions)


@router.post("/weighting-input", response_model=WeightingHandoffResponse)
def create_weighting_input(request: WeightingHandoffRequest) -> WeightingHandoffResponse:
    known_keys = {criterion.key for criterion in request.criteria}
    invalid_answers = [
        answer.selected_key for answer in request.tradeoff_answers if answer.selected_key not in known_keys
    ]
    if invalid_answers:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Tradeoff answers reference unknown criteria: {invalid_answers}",
        )

    REQUIREMENTS_DIR.mkdir(parents=True, exist_ok=True)
    output_path = REQUIREMENTS_DIR / f"{uuid4()}_weighting_input.json"
    payload = {
        "status": "ready_for_weight_calculation",
        "criteria": [criterion.model_dump(mode="json") for criterion in request.criteria],
        "tradeoff_answers": [answer.model_dump(mode="json") for answer in request.tradeoff_answers],
    }
    output_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    return WeightingHandoffResponse(
        status="ready_for_weight_calculation",
        weighting_input_storage_path=str(output_path),
        criteria=request.criteria,
        tradeoff_answers=request.tradeoff_answers,
    )


def _find_next_different_category(criteria: list, start_index: int):
    left = criteria[start_index]
    for offset in range(1, len(criteria)):
        right = criteria[(start_index + offset) % len(criteria)]
        if right.key != left.key and right.category != left.category:
            return right
    return None
