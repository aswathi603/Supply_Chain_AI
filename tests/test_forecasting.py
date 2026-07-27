"""
Forecasting Tests
"""

from forecasting.demand_forecasting import (
    forecast_next_weeks,
)


def test_forecast_shape():

    df = forecast_next_weeks(3)

    assert not df.empty

    assert "forecast_units" in df.columns

    assert "product" in df.columns