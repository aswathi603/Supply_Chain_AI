"""
Reporting Service Tests
"""

from services.reporting_service import (
    executive_brief,
)


def test_brief_keys():

    report = executive_brief()

    expected = [

        "generated_at",

        "overall_health",

        "shipments",

        "inventory",

        "orders",

        "incidents",

        "warehouses",

    ]

    for key in expected:

        assert key in report