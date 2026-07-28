"""
Inventory Agent
"""
from langsmith import traceable

from agents.base_agent import execute_agent, build_context

from prompts.inventory_prompt import PROMPT

from tools.inventory_tools import (
    get_summary,
    get_low_stock,
)

@traceable(name="Inventory Agent")
def run(query: str) -> str:

    context = build_context(
        ("Inventory Summary", get_summary()),
        ("Low Stock Products", get_low_stock()),
    )

    return execute_agent(
        prompt=PROMPT,
        query=query,
        context=context,
        agent_name="Inventory Agent",
    )