import json
from fastapi import APIRouter, HTTPException, status
from pathlib import Path
from pydantic import BaseModel
from app.weighted_metrics.matrix_calc import build_comparison_matrix
from app.weighted_metrics.llm_scorer import recommend_vendor

router = APIRouter(prefix="/evaluate", tags=["evaluate"])

class EvaluateRequest(BaseModel):
    weighting_input_storage_path: str 
    normalised_storage_paths: list[str]

@router.post("")
def evaluate(request: EvaluateRequest): 
    #Load weighting input (criteria + tradeoff answers)
    weighting_path = Path(request.weighting_input_storage_path)
    if not weighting_path.exists():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Weighting input file not found"
        )
    weighting_input = json.loads(weighting_path.read_text(encoding="utf-8"))
    criteria = weighting_input["criteria"]
    tradeoff_answers = weighting_input.get("tradeoff_answers", [])

    #Load each normalized quotation
    quotations = []
    for path_str in request.normalised_storage_paths:
        path = Path(path_str)
        if not path.exists():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Normalised quotation file not found: {path_str}"
            )
        quotation_file = json.loads(path.read_text(encoding="utf-8"))
        quotations.append(quotation_file["normalised"]) #NormalisedQuotation
    
    #Build vendor list from quotations
    vendors = [{"name": q["vendor_name"], **q} for q in quotations]

    #Run the matrix
    try: 
        matrix = build_comparison_matrix(
            vendors=vendors,
            criteria=criteria,
            quotations=quotations,
            tradeoff_answers=tradeoff_answers
        )
    
    except Exception as exc: 
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=str(exc)
        ) from exc
    
    rankings = matrix.reset_index().to_dict(orient="records")
    recommendation = recommend_vendor(rankings,criteria)
    
    return {
        "status": "success",
        "rankings": rankings,
        "recommendation": recommendation
    }