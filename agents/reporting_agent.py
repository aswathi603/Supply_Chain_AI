"""
Reporting Agent
"""

from langsmith import traceable

from agents.base_agent import execute_agent, build_context

from prompts.reporting_prompt import PROMPT

from tools.reporting_tools import get_brief

@traceable(name="Reporting Agent")
def run(query: str) -> str:

    context = build_context(
        ("Executive Brief", get_brief()),
    )

    return execute_agent(
        prompt=PROMPT,
        query=query,
        context=context,
        agent_name="Reporting Agent",
    )