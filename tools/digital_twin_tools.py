"""
Digital Twin Tools
"""

from tools.base_tool import execute

from services.digital_twin_service import (

    available_scenarios,

    run_scenario,

    compare_scenarios,

)


def list_scenarios(
    _: str = "",
) -> str:

    return execute(
        available_scenarios
    )


def simulate(
    scenario: str,
) -> str:

    return execute(
        run_scenario,
        scenario,
    )


def compare_all(
    _: str = "",
) -> str:

    return execute(
        compare_scenarios
    )