"""
Warehouse Model
"""

from pydantic import BaseModel, Field


class Warehouse(BaseModel):
    id: str = Field(...)
    name: str = Field(...)
    country: str = Field(...)
    city: str = Field(...)
    lat: float = Field(...)
    lon: float = Field(...)
    capacity_units: int = Field(...)
    used_units: int = Field(...)
    utilization: float = Field(...)
    type: str = Field(...)

    model_config = {
        "from_attributes": True
    }