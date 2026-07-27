"""
Base Tool

Shared helper functions for all tools.
"""

import json
from typing import Any


def serialize(data: Any) -> str:
    """
    Convert Python object to JSON string.
    """

    return json.dumps(
        data,
        indent=2,
        default=str,
    )


def execute(fn, *args, **kwargs) -> str:
    """
    Execute a service function and
    serialize its output.
    """

    try:

        return serialize(
            fn(*args, **kwargs)
        )

    except Exception as ex:

        return serialize({

            "success": False,

            "error": str(ex)

        })