"""
Shipment Tools
"""

from tools.base_tool import execute

from services.shipment_service import (
    summary,
    delayed,
)


def get_summary(_: str = "") -> str:

    return execute(summary)


def get_delayed(_: str = "") -> str:

    return execute(

        lambda: delayed()[:5]

    )