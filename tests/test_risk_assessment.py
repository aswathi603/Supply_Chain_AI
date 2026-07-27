"""
Risk Assessment Tests
"""

from simulations.risk_assessment import run


def test_risk_assessment():

    result = run()

    assert "scenario" in result

    assert "summary" in result

    assert "impact" in result

    assert "recommendation" in result

    assert "confidence" in result