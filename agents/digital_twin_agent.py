"""
Digital Twin Agent
"""

from agents.base_agent import execute_agent, build_context

from prompts.digital_twin_prompt import PROMPT

from tools.digital_twin_tools import list_scenarios

from digital_twin.recommendation_engine import compare_all_scenarios


def run(query: str) -> str:
    """
    Execute the Digital Twin agent.
    """

    # Run all simulations and compare them
    comparison = compare_all_scenarios()

    # Build structured context for the LLM
    context = build_context(
        (
            "Available Simulation Scenarios",
            list_scenarios(),
        ),
        (
            "Scenario Comparison",
            comparison,
        ),
    )

    return execute_agent(
        prompt=PROMPT,
        query=query,
        context=context,
        agent_name="Digital Twin Agent",
    )