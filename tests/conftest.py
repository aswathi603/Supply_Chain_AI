"""
Shared pytest configuration.
"""

import pytest


@pytest.fixture
def sample_query():

    return (

        "Show delayed shipments"

    )