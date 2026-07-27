"""Registry mapping agent name -> prompt module."""
from prompts import (
    system_prompt, supervisor_prompt, shipment_prompt, inventory_prompt,
    supplier_prompt, incident_prompt, recovery_prompt, reporting_prompt,
    digital_twin_prompt,forecasting_prompt
)

PROMPTS = {
    "system": system_prompt.PROMPT,
    "supervisor": supervisor_prompt.PROMPT,
    "shipment": shipment_prompt.PROMPT,
    "inventory": inventory_prompt.PROMPT,
    "supplier": supplier_prompt.PROMPT,
    "incident": incident_prompt.PROMPT,
    "recovery": recovery_prompt.PROMPT,
    "reporting": reporting_prompt.PROMPT,
    "digital_twin": digital_twin_prompt.PROMPT,
    "forecasting": forecasting_prompt.PROMPT,
}