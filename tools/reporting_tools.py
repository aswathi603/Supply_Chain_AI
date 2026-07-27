"""
Reporting Tools
"""

from tools.base_tool import execute

from services.reporting_service import executive_brief


def get_brief(_: str = "") -> str:

    return execute(
        executive_brief
    )