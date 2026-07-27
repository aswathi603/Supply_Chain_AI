"""
Route Tools
"""

from tools.base_tool import execute

from api.mock_loader import api_get


def list_routes(_: str = "") -> str:

    return execute(
        api_get,
        "routes",
    )