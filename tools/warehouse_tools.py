"""
Warehouse Tools
"""

from tools.base_tool import execute

from services.warehouse_service import summary


def get_summary(_: str = "") -> str:

    return execute(summary)