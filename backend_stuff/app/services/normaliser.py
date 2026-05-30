import json
import os
import re
from typing import Any

from pydantic import ValidationError
import requests

from app.schemas.metrics import NormalisedMetricsTemplate
from app.schemas.quotation import NormalisedQuotation
from app.schemas.requirements import RequirementsDiscoveryResult
from app.schemas.upload import FileKind
from app.services.file_parser import ParsedDocument


class NormalisationError(Exception):
    pass


def build_normalisation_prompt(kind: FileKind, parsed: ParsedDocument) -> str:
    if kind == FileKind.metrics_template:
        return _metrics_prompt(parsed)
    return _quotation_prompt(parsed)


def normalise_document(
    kind: FileKind,
    parsed: ParsedDocument,
) -> tuple[NormalisedQuotation | NormalisedMetricsTemplate, dict[str, Any]]:
    prompt = build_normalisation_prompt(kind, parsed)
    raw_output = _call_llm(prompt)
    json_payload = _extract_json_object(raw_output)

    try:
        if kind == FileKind.metrics_template:
            return NormalisedMetricsTemplate.model_validate(json_payload), json_payload
        return NormalisedQuotation.model_validate(json_payload), json_payload
    except ValidationError as exc:
        raise NormalisationError(f"The model returned JSON, but it did not match the schema: {exc}") from exc


def generate_metrics_from_context(
    context: dict[str, Any],
) -> tuple[NormalisedMetricsTemplate, dict[str, Any]]:
    raw_output = _call_llm(_guided_metrics_prompt(context))
    json_payload = _extract_json_object(raw_output)

    try:
        return NormalisedMetricsTemplate.model_validate(json_payload), json_payload
    except ValidationError as exc:
        raise NormalisationError(f"The model returned metrics JSON, but it did not match the schema: {exc}") from exc


def generate_requirements_criteria(
    context: dict[str, Any],
) -> tuple[RequirementsDiscoveryResult, dict[str, Any]]:
    raw_output = _call_llm(_requirements_discovery_prompt(context))
    json_payload = _extract_json_object(raw_output)

    try:
        return RequirementsDiscoveryResult.model_validate(json_payload), json_payload
    except ValidationError as exc:
        raise NormalisationError(
            f"The model returned requirements JSON, but it did not match the schema: {exc}"
        ) from exc


def _call_llm(prompt: str) -> str:
    api_base_url = os.getenv("LLM_API_BASE_URL", "https://openrouter.ai/api/v1").rstrip("/")
    api_key = os.getenv("OPENROUTER_API_KEY") or os.getenv("LLM_API_KEY")
    model_name = os.getenv("LLM_MODEL", "google/gemini-3.1-flash-lite")

    if not api_key:
        raise NormalisationError("Set OPENROUTER_API_KEY or LLM_API_KEY before calling /normalise.")

    request_body: dict[str, Any] = {
        "model": model_name,
        "temperature": 0,
        "messages": [
            {
                "role": "system",
                "content": "You extract procurement data. Return only valid JSON and no prose.",
            },
            {"role": "user", "content": prompt},
        ],
    }

    if os.getenv("LLM_REASONING_ENABLED", "").lower() in {"1", "true", "yes"}:
        request_body["reasoning"] = {"enabled": True}

    response = requests.post(
        f"{api_base_url}/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json=request_body,
        timeout=90,
    )

    try:
        response.raise_for_status()
    except requests.HTTPError as exc:
        raise NormalisationError(f"LLM API request failed: {response.text[:500]}") from exc

    payload = response.json()
    try:
        text = payload["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as exc:
        raise NormalisationError(f"LLM API returned an unexpected response shape: {payload}") from exc

    if not text:
        raise NormalisationError("LLM API returned an empty response.")

    return text


def _extract_json_object(raw_output: str) -> dict[str, Any]:
    cleaned = raw_output.strip()
    cleaned = re.sub(r"^```(?:json)?", "", cleaned).strip()
    cleaned = re.sub(r"```$", "", cleaned).strip()

    try:
        payload = json.loads(cleaned)
    except json.JSONDecodeError as exc:
        raise NormalisationError(f"The model did not return valid JSON: {raw_output[:500]}") from exc

    if not isinstance(payload, dict):
        raise NormalisationError("The model returned JSON, but the top-level value was not an object.")

    return payload


def _quotation_prompt(parsed: ParsedDocument) -> str:
    return f"""
You are normalising a vendor quotation for a procurement decision system.

Return only valid JSON with this shape:
{{
  "vendor_name": string | null,
  "currency": string | null,
  "quote_valid_until": string | null,
  "shipping_cost": number | null,
  "discount": number | null,
  "payment_terms": string | null,
  "items": [
    {{
      "product_name": string | null,
      "sku": string | null,
      "quantity": number | null,
      "unit_price": number | null,
      "total_price": number | null,
      "delivery_days": number | null,
      "warranty_months": number | null,
      "certifications": [string],
      "notes": string | null
    }}
  ],
  "risk_flags": [string]
}}

Rules:
- Do not invent missing values. Use null when unsure.
- Convert dates to ISO format when possible.
- Convert lead times to days and warranties to months.
- Preserve useful caveats in risk_flags.

Document text:
{parsed.text[:12000]}
""".strip()


def _metrics_prompt(parsed: ParsedDocument) -> str:
    return f"""
You are normalising a company procurement scoring template.

The matrix has exactly four fixed categories:
- functional
- financial
- risks
- strategic

The subcategories inside those categories are what actually get scored.
Examples:
- functional: features, integrations, scalability
- financial: subscription_cost, migration_cost
- risks: security, gdpr_compliance, vendor_stability
- strategic: sustainability, data_residency

Return only valid JSON with this shape:
{{
  "categories": [
    {{
      "category": "functional" | "financial" | "risks" | "strategic",
      "category_weight": number | null,
      "subcategories": {{
        "snake_case_subcategory_key": {{
          "name": string,
          "score": integer from 1 to 5,
          "direction": "higher_is_better" | "lower_is_better" | null,
          "description": string | null,
          "weight": number | null
        }}
      }}
    }}
  ],
  "metrics": [
    {{
      "name": string,
      "weight": number,
      "direction": "higher_is_better" | "lower_is_better",
      "description": string | null,
      "category": "functional" | "financial" | "risks" | "strategic",
      "score": integer from 1 to 5
    }}
  ]
}}

Rules:
- Always use these four categories: functional, financial, risks, strategic.
- The subcategories are the scored dimensions, not the four categories themselves.
- If the source gives scores or importance ratings for subcategories, preserve them as score values from 1 to 5.
- If the source gives weights/percentages, convert them to decimals.
- Keep subcategory keys snake_case.
- Do not add subcategories that are not present in the source.
- The flat metrics list should mirror the same subcategories for easy scoring.

Document text:
{parsed.text[:12000]}
""".strip()


def _guided_metrics_prompt(context: dict[str, Any]) -> str:
    return f"""
You are helping a procurement team create a weighted decision matrix.

The four top-level categories are fixed:
- functional
- financial
- risks
- strategic

The subcategories inside each category are what actually get rated/scored.
Use these as the default subcategory set unless the user context clearly requires changes:
- functional: features, integrations, scalability
- financial: subscription_cost, migration_cost
- risks: security, gdpr_compliance, vendor_stability
- strategic: sustainability, data_residency

Return only valid JSON with this shape:
{{
  "categories": [
    {{
      "category": "functional" | "financial" | "risks" | "strategic",
      "category_weight": number,
      "subcategories": {{
        "snake_case_subcategory_key": {{
          "name": string,
          "score": integer from 1 to 5,
          "direction": "higher_is_better" | "lower_is_better" | null,
          "description": string | null,
          "weight": number
        }}
      }}
    }}
  ],
  "metrics": [
    {{
      "name": string,
      "weight": number,
      "direction": "higher_is_better" | "lower_is_better",
      "description": string | null,
      "category": "functional" | "financial" | "risks" | "strategic",
      "score": integer from 1 to 5
    }}
  ]
}}

Rules:
- Use exactly four categories: functional, financial, risks, strategic.
- Create/rate subcategories inside those categories.
- score means user/business importance of that subcategory on a 1 to 5 scale.
- weight should be a decimal. All flat metrics weights should sum to 1.0.
- Category weights should also sum to 1.0.
- The flat metrics list must mirror every subcategory from categories.
- Do not include prose or markdown.

User context:
{json.dumps(context, indent=2)}
""".strip()


def _requirements_discovery_prompt(context: dict[str, Any]) -> str:
    return f"""
You are acting like a procurement consultant.

Create draft decision criteria for a purchase. Do not create weights. Do not score vendors.
The user will later answer tradeoff questions, and another service will calculate weights.

Use these four fixed categories:
- functional
- financial
- risks
- strategic

Return only valid JSON with this shape:
{{
  "criteria": [
    {{
      "key": "snake_case_key",
      "category": "functional" | "financial" | "risks" | "strategic",
      "label": string,
      "description": string | null,
      "score": integer from 1 to 5
    }}
  ]
}}

Rules:
- Generate 6 to 10 criteria total.
- Include only criteria relevant to the user's purchase context.
- If normalised quotations are provided, use them as extra context for practical criteria.
- Prefer practical procurement criteria, not vague values.
- Use labels that are short and UI-friendly.
- score is a draft importance score from 1 to 5. Use 3 for normal, 4 for important, 5 for critical.
- Do not include weights, markdown, or prose.

Helpful defaults:
- functional: features, integrations, scalability, implementation_effort
- financial: subscription_cost, migration_cost, total_cost_of_ownership
- risks: security, gdpr_compliance, vendor_stability, lock_in_risk
- strategic: sustainability, data_residency, esg_transparency, strategic_fit

User context:
{json.dumps(context, indent=2)}
""".strip()
