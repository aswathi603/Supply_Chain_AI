"""
Simulation Tests
"""

from services.digital_twin_service import (
    run_scenario,
)


def test_rerouting():

    result = run_scenario(

        "Shipment Rerouting",

        new_mode="Air",

    )

    assert "scenario" in result

    assert "summary" in result

    assert "before" in result

    assert "after" in result

    assert "impact" in result

    assert "recommendation" in result

    assert "confidence" in result