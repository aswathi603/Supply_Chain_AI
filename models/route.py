"""
Route Model
"""

from pydantic import BaseModel, Field


class Route(BaseModel):
    id: str = Field(...)
    from_: str = Field(alias="from")
    to: str = Field(...)
    mode: str = Field(...)
    distance_km: float = Field(...)
    avg_days: float = Field(...)
    cost_per_container_usd: float = Field(...)
    co2_kg_per_container: float = Field(...)
    reliability: float = Field(...)

    model_config = {
        "populate_by_name": True,
        "from_attributes": True,
    }