"""
Router Module

Routes user queries to the appropriate CrisisOps AI agent.
Returns "unsupported" for questions outside the Supply Chain domain.
"""

from typing import Dict


# ==========================================================
# Supply Chain Keywords
# ==========================================================

KEYWORDS: Dict[str, list[str]] = {

    "shipment": [
        "shipment",
        "ship",
        "shipping",
        "delivery",
        "delay",
        "delayed",
        "transit",
        "route",
        "reroute",
        "tracking",
        "eta",
        "transport",
        "container",
        "freight",
        "cargo",
        "port",
        "customs",
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
        "inventory level",
        "storage",
    ],

    "supplier": [
        "supplier",
        "vendor",
        "manufacturer",
        "procurement",
        "purchase",
        "alternate supplier",
        "replacement supplier",
        "sourcing",
    ],

    "incident": [
        "incident",
        "issue",
        "problem",
        "disruption",
        "weather",
        "strike",
        "damage",
        "risk",
        "critical",
        "customs",
    ],

    "recovery": [
        "recover",
        "recovery",
        "mitigation",
        "resolve",
        "solution",
        "recommend",
        "recommendation",
        "alternative",
        "replan",
    ],

    "reporting": [
        "report",
        "summary",
        "dashboard",
        "analytics",
        "executive",
        "kpi",
        "performance",
        "health",
        "overview",
        "brief",
    ],

    "digital_twin": [
        "simulation",
        "simulate",
        "scenario",
        "digital twin",
        "what if",
        "comparison",
        "compare",
        "rerouting",
    ],

    "forecasting": [
        "forecast",
        "forecasting",
        "prediction",
        "predict",
        "future",
        "trend",
        "next week",
        "next month",
        "growth",
        "capacity",
        "demand",
        "utilization",
    ],
}


# ==========================================================
# Out of Domain Keywords
# ==========================================================

UNSUPPORTED_KEYWORDS = [

    # Programming
    "python",
    "java",
    "javascript",
    "typescript",
    "html",
    "css",
    "react",
    "node",
    "django",
    "flask",
    "spring",
    "sql",
    "mongodb",

    # CS
    "oops",
    "oop",
    "object oriented",
    "algorithm",
    "algorithms",
    "data structure",
    "linked list",
    "stack",
    "queue",
    "tree",
    "graph",
    "operating system",
    "computer network",
    "dbms",

    # AI
    "machine learning",
    "deep learning",
    "cnn",
    "rnn",
    "llm",
    "chatgpt",

    # General knowledge
    "history",
    "physics",
    "chemistry",
    "biology",
    "geography",
    "politics",
    "movie",
    "movies",
    "music",
    "cricket",
    "football",
    "ipl",
    "fifa",
    "weather today",
    "news",

]


# ==========================================================
# Route Query
# ==========================================================

def route(query: str) -> str:
    """
    Returns the best matching agent.
    Returns 'unsupported' for non-supply-chain queries.
    """

    if not query:
        return "unsupported"

    query = query.lower().strip()

    # ---------------------------------------
    # Explicit Out-of-Domain Detection
    # ---------------------------------------

    for keyword in UNSUPPORTED_KEYWORDS:

        if keyword in query:

            return "unsupported"

    # ---------------------------------------
    # Score all supply-chain agents
    # ---------------------------------------

    scores = {}

    for agent, words in KEYWORDS.items():

        score = 0

        for word in words:

            if word in query:

                score += 1

        scores[agent] = score

    best_agent = max(scores, key=scores.get)

    # No supply-chain keyword found

    if scores[best_agent] == 0:

        return "unsupported"

    return best_agent


# ==========================================================
# Confidence Score
# ==========================================================

def confidence(query: str) -> float:
    """
    Returns routing confidence.
    """

    query = query.lower()

    total = 0
    best = 0

    for words in KEYWORDS.values():

        score = sum(

            1

            for word in words

            if word in query

        )

        total += score

        best = max(best, score)

    if total == 0:

        return 0.0

    return round(best / total, 2)