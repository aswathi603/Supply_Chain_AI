"""
Tests for Supervisor Agent
"""

from agents.supervisor_agent import run


def test_router_shipment():

    result = run(
        "Which shipments are delayed?"
    )

    assert result["agent"] == "shipment"

    assert isinstance(
        result["response"],
        str,
    )


def test_router_supplier():

    result = run(
        "Find alternate suppliers for electronics"
    )

    assert result["agent"] == "supplier"


def test_router_reporting():

    result = run(
        "Generate executive KPI report"
    )

    assert result["agent"] == "reporting"