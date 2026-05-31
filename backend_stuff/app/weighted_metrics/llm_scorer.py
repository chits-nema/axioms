import json
from app.services.normaliser import NormalisationError, _call_llm

def score_vendor_on_metric(
    vendor: dict, 
    metric: dict,
    quotation: dict,
    tradeoff_answers: list) -> dict: 
    """
    Scores a single vendor on a single metric.
    
    metric looks like:
    {
        "key": "gdpr_compliance",
        "category": "risks",
        "label": "GDPR Compliance",
        "description": "Adherence to EU data protection regulations.",
        "score": 5   <-- this is actually the buyer's weight, not a vendor score
    }
    """

    #count the times metric was chosen in tradeoffs
    tradeoff_count = sum(
        1 for answer in tradeoff_answers
        if answer["selected_key"] == metric["key"]
    )

    prompt = f"""

    You are an impartial B2B purchasing evaluator.

    You are scoring a vendor on a single metric based on:
    1. The vendor's catalogue profile
    2. The actual quotation the vendor submitted
    3. How much the buyer prioritized this metric

    === METRIC TO EVALUATE ===
    Name: {metric["label"]}
    Category: {metric["category"]}
    Description: {metric["description"]}
    Buyer importance (1-5): {metric["score"]}
    Times chosen in tradeoff survey: {tradeoff_count}

    Vendor profile: 
    {json.dumps(vendor, indent=2)}
    
    Vendor quotation:
    {json.dumps(quotation, indent=2)}

    Score this vendor on "{metric}" from 0 to 10, where: 
    - 0 = extremely poor / no capability
    - 5 = meets basic expectations
    - 10 = excellent / industry-leading

    Base your score strictly on evidence from vendor profile and quotation. Do not invent facts.

    Respond ONLY in this JSON format, no other text: 
    {{
        "score": <number 0-10>, 
        "reasoning": "<1-2 sentence justification>"
    }}
    """

    raw_output = _call_llm(prompt)

    return json.loads(raw_output)

def recommend_vendor(matrix_records:list[dict], criteria: list[dict]) -> dict: 
    """Takes the ranked matrix and asks LLM to give a final vendor recommendation
    matrix_records: rankings list from matrix.reset_index().to_dict(orient="records")
    criteria: the original criteria list w/ descriptions
    """

    prompt = f"""
    You are an impartial B2B procurement advisor. 
    Based on the following vendor evaluation matrix, recommend the best vendor and explain why.
    Consider the weighted scores, individual metric scores, and the buyer's priorities.

    Criteria used: 
    {json.dumps(criteria, indent=2)}

    Vendor evaluation results:
    {json.dumps(criteria, indent=2)}
    
    Respond ONLY in this JSON format: 
    {{
        "recommend_vendor": "<vendor name>"
        "reasoning": "<2-3 sentence explanation citing specific scores and buyer priorities>",
        "trade_offs": "<1-2 sentence note on what the buyer gives up by not choosing the runner-up>"
    }}
    """

    raw_output = _call_llm(prompt)
    return json.loads(raw_output)