"""
Supplier Model
"""

from typing import List

from pydantic import BaseModel, Field


class Supplier(BaseModel):
    id: str = Field(...)
    name: str = Field(...)
    country: str = Field(...)
    city: str = Field(...)
    lat: float = Field(...)
    lon: float = Field(...)
    tier: str = Field(...)
    reliability_score: float = Field(...)
    avg_lead_time_days: int = Field(...)
    categories: List[str] = Field(default_factory=list)
    risk_level: str = Field(...)
    on_time_rate: float = Field(...)
    annual_spend_usd: float = Field(...)

    model_config = {
        "from_attributes": True
    }