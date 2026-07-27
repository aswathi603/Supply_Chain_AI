from services.supplier_service import alternates_for
from api.supplier_api import get_supplier

def run(supplier_id: str = "SUP-1001", category: str = None):
    src = get_supplier(supplier_id) or {}
    cat = category or (src.get("categories") or ["Electronics"])[0]
    alts = alternates_for(cat)[:3]
    return {
        "summary": f"Replace {src.get('name', supplier_id)} for category '{cat}'",
        "candidates": alts,
        "recommendation": alts[0]["id"] if alts else None,
        "confidence": 0.78,
    }
