"""
Shipment Model
"""

from pydantic import BaseModel, Field


class Shipment(BaseModel):
    id: str = Field(...)
    supplier_id: str = Field(...)
    origin: str = Field(...)
    destination: str = Field(...)
    mode: str = Field(...)
    status: str = Field(...)
    eta_days: int = Field(...)
    delay_days: int = Field(...)
    value_usd: float = Field(...)
    priority: str = Field(...)
    product: str = Field(...)
    units: int = Field(...)

    model_config = {
        "from_attributes": True
    }