"""
Scenario Comparison Engine
"""


def compare(
    baseline: dict,
    candidate: dict,
) -> dict:

    comparison = {}

    for key, value in candidate.items():

        old = baseline.get(key)

        if isinstance(value, (int, float)) and isinstance(old, (int, float)):

            comparison[key] = {
                "before": old,
                "after": value,
                "difference": round(value - old, 2),
            }

    return comparison