"""
Supervisor Agent

Acts as the central coordinator of CrisisOps AI.
Determines the appropriate specialist agent,
executes it, and returns the response.
"""

from langsmith import traceable

from datetime import datetime
from agents import unsupported_agent

from agents import (
    router,
    shipment_agent,
    inventory_agent,
    supplier_agent,
    incident_agent,
    recovery_agent,
    reporting_agent,
    digital_twin_agent,
    forecasting_agent
)

# ============================================================
# Agent Registry
# ============================================================

REGISTRY = {

    "shipment": shipment_agent.run,
    "inventory": inventory_agent.run,
    "supplier": supplier_agent.run,
    "incident": incident_agent.run,
    "recovery": recovery_agent.run,
    "reporting": reporting_agent.run,
    "digital_twin": digital_twin_agent.run,
    "forecasting": forecasting_agent.run,

    "unsupported": unsupported_agent.run,

}


# ============================================================
# Supervisor
# ============================================================

@traceable(name="Supervisor Agent")
def run(query: str) -> dict:
    """
    Routes the query to the correct specialist agent.

    Returns:
    {
        "agent": "...",
        "confidence": 0.85,
        "timestamp": "...",
        "success": True,
        "response": "..."
    }
    """

    try:

        # Decide which agent should handle the request
        agent = router.route(query)

        confidence = router.confidence(query)

        # Get the corresponding function
        agent_function = REGISTRY.get(
            agent,
            reporting_agent.run,
        )

        # Execute specialist agent
        response = agent_function(query)

        return {

            "success": True,

            "agent": agent,

            "confidence": confidence,

            "timestamp": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

            "response": response,
        }

    except Exception as ex:

        return {

            "success": False,

            "agent": "supervisor",

            "confidence": 0.0,

            "timestamp": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

            "response":
                "Unable to process the request.",

            "error": str(ex),
        }