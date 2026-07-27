"""
Order Model
"""

from pydantic import BaseModel, Field


class Order(BaseModel):
    id: str = Field(...)
    customer_id: str = Field(...)
    customer_name: str = Field(...)
    product: str = Field(...)
    units: int = Field(...)
    value_usd: float = Field(...)
    priority: str = Field(...)
    promised_date: str = Field(...)
    status: str = Field(...)

    model_config = {
        "from_attributes": True
    }