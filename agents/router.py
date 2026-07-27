"""
Router Module

Routes the user query to the appropriate specialist agent.
"""

from typing import Dict

# ==========================================================
# Agent Keywords
# ==========================================================

KEYWORDS: Dict[str, list[str]] = {

    "shipment": [
        "shipment",
        "ship",
        "delivery",
        "delay",
        "transit",
        "route",
        "reroute",
        "tracking",
        "eta",
        "transport",
    ],

    "inventory": [
        "inventory",
        "stock",
        "warehouse",
        "sku",
        "quantity",
        "low stock",
        "reorder",
        "availability",
    ],

    "supplier": [
        "supplier",
        "vendor",
        "manufacturer",
        "procurement",
        "purchase",
        "alternate supplier",
        "sourcing",
    ],

    "incident": [
        "incident",
        "issue",
        "problem",
        "disruption",
        "weather",
        "customs",
        "port",
        "strike",
        "damage",
    ],

    "recovery": [
        "recover",
        "recovery",
        "mitigation",
        "resolve",
        "recommend",
        "solution",
        "alternative",
        "replan",
    ],

    "reporting": [
        "report",
        "summary",
        "dashboard",
        "analytics",
        "kpi",
        "executive",
        "performance",
    ],

    "digital_twin": [
        "simulate",
        "simulation",
        "scenario",
        "digital twin",
        "what if",
        "compare",
        "forecast",
    ],
    
    "forecasting": [

        "forecast",

        "prediction",

        "predict",

        "future",

        "next week",

        "next month",

        "trend",

        "growth",

        "demand",

        "capacity",

    ],
}


# ==========================================================
# Route Query
# ==========================================================

def route(query: str) -> str:
    """
    Returns the best matching agent.

    Args:
        query: User query

    Returns:
        Agent name
    """

    if not query:
        return "reporting"

    query = query.lower()

    scores = {}

    for agent, words in KEYWORDS.items():

        score = 0

        for word in words:

            if word in query:
                score += 1

        scores[agent] = score

    best_agent = max(scores, key=scores.get)

    if scores[best_agent] == 0:
        return "reporting"

    return best_agent


# ==========================================================
# Confidence (Useful for Supervisor)
# ==========================================================

def confidence(query: str) -> float:
    """
    Returns routing confidence between 0 and 1.
    """

    query = query.lower()

    total_matches = 0

    best = 0

    for words in KEYWORDS.values():

        score = sum(1 for word in words if word in query)

        total_matches += score

        if score > best:
            best = score

    if total_matches == 0:
        return 0.0

    return round(best / total_matches, 2)