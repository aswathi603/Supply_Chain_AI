from api.transportation_api import modes_df

def run(distance_km: float = 10000):
    df = modes_df().copy()
    df["cost_usd"] = (df["avg_cost_per_km_usd"] * distance_km).round(0)
    df["days"] = (df["avg_days_per_1000km"] * (distance_km/1000)).round(1)
    df["co2_kg"] = (df["co2_kg_per_1000km"] * (distance_km/1000)).round(0)
    return {"summary": f"Mode comparison for {distance_km} km",
            "table": df.to_dict(orient="records"),
            "confidence": 0.9}
