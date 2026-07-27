"""
Failed Workflow Tracker
"""

from pathlib import Path
import json

FAILED_RUNS = Path("logs/failed_runs.json")


def failed_runs():

    if not FAILED_RUNS.exists():

        return []

    try:

        with open(
            FAILED_RUNS,
            "r",
            encoding="utf-8",
        ) as f:

            return json.load(f)

    except Exception:

        return []