"""Digital twin: build a serializable state snapshot of the supply chain."""
from api.mock_loader import api_get

def snapshot():
    return {
        "suppliers": api_get("suppliers"),
        "shipments": api_get("shipments"),
        "warehouses": api_get("warehouses"),
        "inventory": api_get("inventory"),
        "incidents": api_get("incidents"),
        "orders": api_get("orders"),
        "timestamp": datetime.now().isoformat()
    }
