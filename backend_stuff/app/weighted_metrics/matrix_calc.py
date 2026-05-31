import pandas as pd
from app.weighted_metrics.llm_scorer import score_vendor_on_metric

def build_comparison_matrix(
    vendors: list[dict], 
    criteria: list[dict], 
    quotations: list[dict],
    tradeoff_answers: list[dict]) -> pd.DataFrame: 
   
    total = sum(c["score"] for c in criteria)
    for c in criteria: 
        c["weight"] = c["score"] / total if total > 0 else 0

    records = []  # outside the for loop now

    for vendor in vendors: 
        quotation = next(
            (q for q in quotations if q["vendor_name"] == vendor["name"]),  # fixed
            {}
        )
        
        row = {"vendor": vendor["name"]}
        weighted_total = 0.0

        for metric in criteria:
            result = score_vendor_on_metric(vendor, metric, quotation, tradeoff_answers)  # no client
            score = result["score"]

            row[metric["key"]] = score
            row[f"{metric['key']}_reasoning"] = result["reasoning"]
            row[f"{metric['key']}_weighted"] = round(score * metric["weight"], 2)
            weighted_total += score * metric["weight"]
        
        row["weighted_score"] = round(weighted_total, 2)
        records.append(row)
    
    df = pd.DataFrame(records).set_index("vendor")
    return df.sort_values("weighted_score", ascending=False)