"""
Warehouse Utilization Forecast
"""

from api.warehouse_api import warehouses_df

from forecasting.base_forecaster import (
    forecast_metadata,
)


def utilization_projection(
    growth_pct: float = 8.0,
):
    """
    Forecast warehouse utilization.
    """

    df = warehouses_df().copy()

    df["projected_utilization"] = (

        df["utilization"]

        * (1 + growth_pct / 100)

    ).clip(
        upper=1.05
    ).round(3)

    return {

        "metadata":
            forecast_metadata(
                "Warehouse Forecast"
            ),

        "forecast":
            df.to_dict(
                orient="records"
            ),

    }