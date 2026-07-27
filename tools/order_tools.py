"""
Order Tools
"""

from tools.base_tool import execute

from services.order_service import (

    at_risk,

    summary,

)


def get_summary(_: str = "") -> str:

    return execute(summary)


def get_at_risk(_: str = "") -> str:

    return execute(at_risk)