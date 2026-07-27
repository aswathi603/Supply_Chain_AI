from api.warehouse_api import warehouses_df

def run(target_util: float = 0.75):
    df = warehouses_df().copy()
    df["gap_units"] = (df["capacity_units"] * (df["utilization"] - target_util)).round(0)
    hot = df[df["gap_units"] > 0].sort_values("gap_units", ascending=False)
    cold = df[df["gap_units"] < 0].sort_values("gap_units")
    return {
        "summary": f"Balance warehouses to {int(target_util*100)}% utilization",
        "over_capacity": hot[["id", "name", "utilization", "gap_units"]].to_dict(orient="records"),
        "under_capacity": cold[["id", "name", "utilization", "gap_units"]].to_dict(orient="records"),
        "confidence": 0.82,
    }
