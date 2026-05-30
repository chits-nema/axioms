import json
import os
import re
from typing import Any

from pydantic import ValidationError
import requests

from app.schemas.metrics import NormalisedMetricsTemplate
from app.schemas.quotation import NormalisedQuotation
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

Return only valid JSON with this shape:
{{
  "metrics": [
    {{
      "name": string,
      "weight": number,
      "direction": "higher_is_better" | "lower_is_better",
      "description": string | null
    }}
  ]
}}

Rules:
- Weights should be decimals that sum to 1.0 if the source gives percentages.
- Keep the company's metric names, but make them snake_case.
- Do not add metrics that are not present in the source.

Document text:
{parsed.text[:12000]}
""".strip()
