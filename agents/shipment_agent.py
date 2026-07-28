"""
Shipment Agent
"""

from langsmith import traceable

from agents.base_agent import execute_agent, build_context

from prompts.shipment_prompt import PROMPT

from tools.shipment_tools import (
    get_summary,
    get_delayed,
)


@traceable(name="Shipment Agent")
def run(query: str) -> str:

    context = build_context(
        ("Shipment Summary", get_summary()),
        ("Delayed Shipments", get_delayed()),
    )

    return execute_agent(
        prompt=PROMPT,
        query=query,
        context=context,
        agent_name="Shipment Agent",
    )