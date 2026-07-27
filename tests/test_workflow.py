"""
Workflow Tests
"""

from graph.workflow import (
    run_workflow,
)


def test_workflow_returns_response():

    result = run_workflow(

        "Generate executive report"

    )

    assert "agent" in result

    assert "response" in result