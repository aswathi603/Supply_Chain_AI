"""
Recovery Agent
"""

from langsmith import traceable

from agents.base_agent import execute_agent, build_context

from prompts.recovery_prompt import PROMPT

from tools.recovery_tools import get_plan

@traceable(name="Incident Agent")
def run(query: str) -> str:

    context = build_context(
        ("Recovery Plan", get_plan()),
    )

    return execute_agent(
        prompt=PROMPT,
        query=query,
        context=context,
        agent_name="Recovery Agent",
    )