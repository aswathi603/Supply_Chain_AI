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

    fn = REGISTRY.get(

        state["route"],

        REGISTRY["reporting"]

    )

    result = fn(

        state["query"]

    )

    state["response"] = result

    state["requires_approval"] = (

        state["route"]

        ==

        "recovery"

    )

    return state