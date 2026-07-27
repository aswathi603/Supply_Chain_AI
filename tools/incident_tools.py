"""
Incident Tools
"""

from tools.base_tool import execute

from services.incident_service import (

    open_incidents,

    summary,

)


def get_open(_: str = "") -> str:

    return execute(
        open_incidents
    )


def get_summary(_: str = "") -> str:

    return execute(
        summary
    )