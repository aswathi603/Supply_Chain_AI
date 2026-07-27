"""
Incident Agent
"""

from agents.base_agent import execute_agent, build_context

from prompts.incident_prompt import PROMPT

from tools.incident_tools import (
    get_summary,
    get_open,
)


def run(query: str) -> str:

    context = build_context(
        ("Incident Summary", get_summary()),
        ("Open Incidents", get_open()),
    )

    return execute_agent(
        prompt=PROMPT,
        query=query,
        context=context,
        agent_name="Incident Agent",
    )