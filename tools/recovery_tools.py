"""
Recovery Tools
"""

from tools.base_tool import execute

from services.recovery_service import recovery_plan


def get_plan(
    shipment_id: str = "",
) -> str:

    if shipment_id:

        return execute(
            recovery_plan,
            shipment_id,
        )

    return execute(
        recovery_plan
    )