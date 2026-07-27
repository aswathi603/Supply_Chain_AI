"""
Demand Forecasting

Simple trend-based demand forecasting.
"""

import pandas as pd

from api.mock_loader import api_get_df
from forecasting.base_forecaster import forecast_metadata


def forecast_next_weeks(
    weeks: int = 4,
):
    """
    Forecast demand for the next N weeks.
    """

    df = api_get_df("demand")

    forecasts = []

    for product, group in df.groupby("product"):

        actual = group.dropna(
            subset=["actual_units"]
        )

        if actual.empty:
            continue

        average = float(
            actual["actual_units"].mean()
        )

        growth_rate = 1.05

        for week in range(1, weeks + 1):

            forecasts.append(

                {

                    "product": product,

                    "week_offset": week,

                    "forecast_units": round(
                        average * (growth_rate ** week)
                    ),

                }

            )

    return {

        "metadata":
            forecast_metadata(
                "Demand Forecast"
            ),

        "forecast":
            forecasts,

    }