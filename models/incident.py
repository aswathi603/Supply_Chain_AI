"""
Incident Model
"""

from typing import List

from pydantic import BaseModel, Field


class Incident(BaseModel):
    id: str = Field(...)
    type: str = Field(...)
    severity: str = Field(...)
    location: str = Field(...)
    affected_shipments: List[str] = Field(default_factory=list)
    started: str = Field(...)
    status: str = Field(...)
    expected_resolution_days: int = Field(...)
    impact_usd: float = Field(...)

    model_config = {
        "from_attributes": True
    }