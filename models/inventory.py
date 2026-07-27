"""
Inventory Model
"""

from pydantic import BaseModel, Field


class InventoryItem(BaseModel):
    sku: str = Field(...)
    product: str = Field(...)
    warehouse_id: str = Field(...)
    units_on_hand: int = Field(...)
    reorder_point: int = Field(...)
    safety_stock: int = Field(...)
    unit_cost_usd: float = Field(...)
    days_of_supply: int = Field(...)

    model_config = {
        "from_attributes": True
    }