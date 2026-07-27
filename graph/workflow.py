"""
Workflow entry.
"""

from graph.graph_builder import run


def run_workflow(query: str) -> dict:
    """
    Public workflow entry point.
    Used by the UI.
    """

    return run(query)


def execute_workflow(query: str) -> dict:
    """
    Alias for backward compatibility.
    """

    return run_workflow(query)