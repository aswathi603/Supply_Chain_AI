"""
Graph Nodes
"""

from agents.router import route
from agents.supervisor_agent import REGISTRY

from graph.logger import (
    log_query,
    log_route,
    log_agent,
)


def supervisor_node(state):

    log_query(state["query"])

    route_name = route(state["query"])

    log_route(route_name)

    state["route"] = route_name

    return state


def agent_node(state):

    # Handle unsupported questions
    if state["route"] == "unsupported":

        state["response"] = (
            "Sorry, I can't answer that question because it is outside my knowledge domain.\n\n"
            "I am designed specifically for Supply Chain Intelligence and Crisis Management.\n\n"
            "I can help with:\n"
            "• Shipments\n"
            "• Inventory\n"
            "• Suppliers\n"
            "• Warehouses\n"
            "• Logistics\n"
            "• Shipment Delays\n"
            "• Demand Forecasting\n"
            "• Digital Twin Simulations\n"
            "• Recovery Planning\n"
            "• Executive Reporting\n\n"
            "Please ask a supply-chain-related question."
        )

        state["requires_approval"] = False

        return state

    fn = REGISTRY[state["route"]]

    result = fn(state["query"])

    state["response"] = result

    state["requires_approval"] = (
        state["route"] == "recovery"
    )

    return state