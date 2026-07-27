"""
Supplier Tools
"""

from tools.base_tool import execute

from services.supplier_service import (

    top_suppliers,

    risky_suppliers,

    alternates_for,

)


def get_top(_: str = "") -> str:

    return execute(top_suppliers)


def get_risky(_: str = "") -> str:

    return execute(risky_suppliers)


def get_alternates(
    category: str,
) -> str:

    return execute(
        alternates_for,
        category,
    )