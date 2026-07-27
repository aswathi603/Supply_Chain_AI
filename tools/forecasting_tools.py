"""
Forecasting Tools

Provides forecasting capabilities to AI agents.
"""

from tools.base_tool import execute

from forecasting.forecast_service import (
    generate_forecasts,
)

from forecasting.demand_forecasting import (
    forecast_next_weeks,
)

from forecasting.delay_prediction import (
    predict_delays,
)

from forecasting.inventory_forecasting import (
    days_of_supply_outlook,
)

from forecasting.transportation_cost import (
    cost_outlook,
)

from forecasting.warehouse_utilization import (
    utilization_projection,
)

from forecasting.business_impact import (
    business_impact,
)


def get_all_forecasts(_: str = "") -> str:
    """
    Generate every available forecast.
    """

    return execute(
        generate_forecasts
    )


def get_demand_forecast(_: str = "") -> str:
    """
    Demand forecast.
    """

    return execute(
        forecast_next_weeks
    )


def get_delay_forecast(_: str = "") -> str:
    """
    Shipment delay forecast.
    """

    return execute(
        predict_delays
    )


def get_inventory_forecast(_: str = "") -> str:
    """
    Inventory outlook.
    """

    return execute(
        days_of_supply_outlook
    )


def get_transportation_forecast(_: str = "") -> str:
    """
    Transportation cost forecast.
    """

    return execute(
        cost_outlook
    )


def get_warehouse_forecast(_: str = "") -> str:
    """
    Warehouse utilization forecast.
    """

    return execute(
        utilization_projection
    )


def get_business_impact(_: str = "") -> str:
    """
    Business impact forecast.
    """

    return execute(
        business_impact
    )