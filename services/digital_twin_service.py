"""
Digital Twin Service

Runs supply chain simulations and compares
multiple recovery strategies.
"""

from typing import Dict, List

from simulations import (
    shipment_rerouting,
    supplier_replacement,
    demand_spike,
    warehouse_capacity,
    inventory_redistribution,
    customs_delay,
    transportation_comparison,
    premium_customer_priority,
    risk_assessment
)

# ==========================================================
# Scenario Registry
# ==========================================================

SCENARIOS = {

    "Shipment Rerouting":
        shipment_rerouting.run,

    "Supplier Replacement":
        supplier_replacement.run,

    "Demand Spike":
        demand_spike.run,

    "Warehouse Capacity":
        warehouse_capacity.run,

    "Inventory Redistribution":
        inventory_redistribution.run,

    "Customs Delay":
        customs_delay.run,

    "Transportation Comparison":
        transportation_comparison.run,

    "Premium Customer Priority":
        premium_customer_priority.run,

    "Risk Assessment": 
        risk_assessment.run,
}


# ==========================================================
# Run Single Scenario
# ==========================================================

def run_scenario(
    scenario_name: str,
    **params,
) -> Dict:
    """
    Execute one Digital Twin scenario.
    """

    simulation = SCENARIOS.get(scenario_name)

    if simulation is None:

        return {

            "success": False,

            "scenario": scenario_name,

            "error":
                f"Unknown scenario '{scenario_name}'"

        }

    try:

        result = simulation(**params)

        result["success"] = True

        result["scenario"] = scenario_name

        return result

    except Exception as ex:

        return {

            "success": False,

            "scenario": scenario_name,

            "error": str(ex),

        }


# ==========================================================
# Run All Scenarios
# ==========================================================

def run_all_scenarios(
    **params,
) -> List[Dict]:
    """
    Execute every available simulation.
    """

    results = []

    for scenario_name in SCENARIOS:

        result = run_scenario(
            scenario_name,
            **params,
        )

        results.append(result)

    return results


# ==========================================================
# Compare Scenarios
# ==========================================================

def compare_scenarios(
    **params,
) -> Dict:
    """
    Compare all scenarios and return
    the best recommendation.
    """

    simulations = run_all_scenarios(
        **params
    )

    valid = [

        simulation

        for simulation in simulations

        if simulation.get("success")

    ]

    if not valid:

        return {

            "recommended": None,

            "alternatives": simulations,

        }

    recommended = max(

        valid,

        key=lambda simulation: (

            simulation.get(
                "service_level_uplift_pct",
                0,
            )

            -

            simulation.get(
                "extra_cost_usd",
                0,
            ) / 10000

            +

            simulation.get(
                "time_saved_days",
                0,
            )

        )

    )

    return {

        "recommended":

            recommended,

        "alternatives":

            simulations,

    }


# ==========================================================
# List Scenarios
# ==========================================================

def available_scenarios():

    return list(
        SCENARIOS.keys()
    )