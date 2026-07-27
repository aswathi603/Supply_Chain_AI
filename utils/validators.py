"""
Validation Helpers
"""

import re


def is_valid_id(

    value: str,

    prefix: str,

):

    pattern = rf"^{prefix}-\d+$"

    return bool(

        re.match(

            pattern,

            value,

        )

    )


def is_positive(

    value,

):

    try:

        return float(value) >= 0

    except Exception:

        return False