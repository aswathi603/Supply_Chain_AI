"""
Forecast Service
"""

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


def generate_forecasts():

    return {

        "demand":

            forecast_next_weeks(),

        "delay":

            predict_delays(),

        "inventory":

            days_of_supply_outlook(),

        "transportation":

            cost_outlook(),

        "warehouse":

            utilization_projection(),

        "business":

            business_impact(),

    }