"""
Structured output parser.
"""

import json


def parse_json(data):

    try:
        return json.loads(data)

    except Exception:

        return {
            "raw": str(data)
        }