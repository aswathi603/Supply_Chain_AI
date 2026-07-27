"""
Forecasting Agent
"""

from agents.base_agent import (
    execute_agent,
    build_context,
)

from prompts.forecasting_prompt import PROMPT

from tools.forecasting_tools import (
    get_all_forecasts,
)


def run(
    query: str,
) -> str:

    context = build_context(

        (
            "Forecast Results",
            get_all_forecasts(),
        ),

    )

    return execute_agent(

        prompt=PROMPT,

        query=query,

        context=context,

        agent_name="Forecasting Agent",

    )