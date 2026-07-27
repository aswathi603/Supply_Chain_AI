"""
Confidence Engine
"""


def score(result: dict) -> float:

    confidence = 0.50

    if result.get("summary"):
        confidence += 0.15

    if result.get("delta"):
        confidence += 0.15

    if result.get("recommendation"):
        confidence += 0.20

    return round(min(confidence, 1.0), 2)