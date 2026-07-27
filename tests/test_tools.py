"""
Shipment Tool Tests
"""

import json

from tools.shipment_tools import (
    get_summary,
)


def test_shipment_summary_tool():

    summary = json.loads(

        get_summary()

    )

    assert "total_shipments" in summary

    assert "delayed" in summary

    assert "value_at_risk_usd" in summary