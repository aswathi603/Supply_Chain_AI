from api.inventory_api import inventory_df

def run(product: str = "Semiconductors", spike_pct: int = 40):
    df = inventory_df()
    hits = df[df["product"] == product].copy()
    hits["new_days_of_supply"] = (hits["days_of_supply"] / (1 + spike_pct/100.0)).round(1)
    stockouts = int((hits["new_days_of_supply"] < 7).sum())
    return {
        "summary": f"+{spike_pct}% demand on {product}",
        "impact": hits[["sku", "warehouse_id", "days_of_supply", "new_days_of_supply"]].to_dict(orient="records"),
        "stockout_risk_lines": stockouts,
        "confidence": 0.79,
    }