"""
Human approval node.
"""


def request_approval(state):

    if not state.get(
        "requires_approval",
        False,
    ):

        state["approved"] = True

        return state

    # UI will update this later.
    state["approved"] = False

    return state