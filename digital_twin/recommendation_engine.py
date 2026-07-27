"""
Recommendation Engine

Compares all available Digital Twin scenarios
and recommends the best recovery strategy.
"""

from services.digital_twin_service import (
    SCENARIOS,
    run_scenario,
)

from digital_twin.confidence_engine import score


def compare_all_scenarios():
    """
    Run every available simulation scenario and compare them.

    Returns:
        {
            "recommended": {...},
            "alternatives": [...],
        }
    """

    results = []

    for scenario_name in SCENARIOS.keys():

        simulation = run_scenario(scenario_name)

        simulation["scenario"] = scenario_name

        simulation["confidence"] = score(simulation)

        results.append(simulation)

    # Highest confidence wins
    recommended = max(
        results,
        key=lambda x: x["confidence"]
    )

    return {
        "recommended": recommended,
        "alternatives": results,
    }


def recommend(scenario_name: str):
    """
    Run a single scenario.

    Used when the user explicitly selects one.
    """

    result = run_scenario(scenario_name)

    result["scenario"] = scenario_name

    result["confidence"] = score(result)

    result["recommendation"] = result.get(
        "summary",
        "Recommended based on current operational metrics."
    )

    return result