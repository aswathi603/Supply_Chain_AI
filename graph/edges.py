"""
Graph edges.
"""


def supervisor_edge(state):

    return "agent"


def approval_edge(state):

    if state.get(
        "approved"
    ):

        return "end"

    return "human"