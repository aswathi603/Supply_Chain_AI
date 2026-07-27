"""
Conditional routing.
"""


def next_step(state):

    if state.get("error"):

        return "end"

    if state.get("requires_approval"):

        return "human"

    return "agent"