"""
Inventory Tools
"""

from tools.base_tool import execute

from services.inventory_service import (
    low_stock,
    summary,
)


def get_summary(_: str = "") -> str:

    return execute(summary)


def get_low_stock(_: str = "") -> str:

    return execute(low_stock)