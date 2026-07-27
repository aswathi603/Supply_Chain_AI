"""
Digital Twin Model
"""

from digital_twin.state_builder import (
    snapshot,
)


class TwinModel:

    def __init__(self):

        self.state = snapshot()

    def refresh(self):

        self.state = snapshot()

        return self.state

    def get_state(self):

        return self.state