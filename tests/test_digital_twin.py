"""
Digital Twin Tests
"""

from digital_twin.twin_models import TwinModel


def test_twin_state():

    twin = TwinModel()

    assert "shipments" in twin.state

    assert "suppliers" in twin.state

    assert "inventory" in twin.state

    assert "warehouses" in twin.state

    assert "incidents" in twin.state