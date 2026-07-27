"""
Customer Model
"""

from pydantic import BaseModel, Field


class Customer(BaseModel):
    id: str = Field(..., description="Customer ID")
    name: str = Field(..., description="Customer name")
    tier: str = Field(..., description="Customer tier")
    region: str = Field(..., description="Operating region")
    annual_revenue_usd: float = Field(..., description="Annual revenue")

    model_config = {
        "from_attributes": True
    }