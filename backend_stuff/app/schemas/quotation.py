from pydantic import BaseModel, Field


class QuotationItem(BaseModel):
    product_name: str | None = None
    sku: str | None = None
    quantity: float | None = None
    unit_price: float | None = None
    total_price: float | None = None
    delivery_days: float | None = None
    warranty_months: float | None = None
    certifications: list[str] = Field(default_factory=list)
    notes: str | None = None


class NormalisedQuotation(BaseModel):
    vendor_name: str | None = None
    currency: str | None = None
    quote_valid_until: str | None = None
    shipping_cost: float | None = None
    discount: float | None = None
    payment_terms: str | None = None
    items: list[QuotationItem] = Field(default_factory=list)
    risk_flags: list[str] = Field(default_factory=list)
