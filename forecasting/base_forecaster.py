"""
Base Forecasting Utilities
"""

from datetime import datetime
from typing import Dict


def forecast_metadata(model_name: str) -> Dict:
    """
    Attach metadata to every forecast.
    """

    return {
        "model": model_name,
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "confidence": 0.90,
    }