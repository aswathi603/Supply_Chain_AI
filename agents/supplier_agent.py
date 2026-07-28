"""
Supplier Agent
"""
from langsmith import traceable

from agents.base_agent import execute_agent, build_context

from prompts.supplier_prompt import PROMPT

from tools.supplier_tools import (
    get_top,
    get_risky,
)

@traceable(name="Supplier Agent")
def run(query: str) -> str:

    context = build_context(
        ("Top Suppliers", get_top()),
        ("Risky Suppliers", get_risky()),
    )

    return execute_agent(
        prompt=PROMPT,
        query=query,
        context=context,
        agent_name="Supplier Agent",
    )