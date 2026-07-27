"""Shipment rerouting simulation."""
from api.shipment_api import shipments_df

def run(shipment_id: str = None, new_mode: str = "Air"):
    df = shipments_df()
    s = df[df["id"] == shipment_id]
    if s.empty:
        s = df[df["status"] == "Delayed"].head(1)
    if s.empty:
        return {"summary": "No shipment to reroute.", "before": {}, "after": {}}
    row = s.iloc[0]
    mode_speed = {"Ocean": 1.0, "Rail": 0.55, "Road": 0.4, "Air": 0.15}
    mode_cost = {"Ocean": 1.0, "Rail": 1.7, "Road": 1.2, "Air": 6.5}
    old_days = int(row["eta_days"] + row["delay_days"])
    new_days = max(1, int(old_days * mode_speed.get(new_mode, 0.5)))
    old_cost = float(row["value_usd"]) * 0.06
    new_cost = old_cost * mode_cost.get(new_mode, 2.0)
    return {
        "summary": f"Reroute {row['id']} via {new_mode}",
        "before": {"mode": row["mode"], "eta_days": old_days, "logistics_cost_usd": round(old_cost, 0)},
        "after":  {"mode": new_mode,   "eta_days": new_days, "logistics_cost_usd": round(new_cost, 0)},
        "delta":  {"time_saved_days": old_days - new_days,
                    "extra_cost_usd": round(new_cost - old_cost, 0),
                    "service_level_uplift_pct": 12 if new_mode == "Air" else 6},
        "confidence": 0.86,
    }
