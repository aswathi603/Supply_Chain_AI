"""
Shared state for LangGraph workflow.
"""

from typing import TypedDict, List, Dict, Optional


class GraphState(TypedDict, total=False):

    query: str

    route: str

    context: str

    response: str

    history: List[Dict]

    tool_output: Dict

    requires_approval: bool

    approved: bool

    error: Optional[str]

    metadata: Dict