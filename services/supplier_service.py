from api.supplier_api import suppliers_df

def top_suppliers(n=5):
    df = suppliers_df().sort_values("reliability_score", ascending=False).head(n)
    return df.to_dict(orient="records")

def risky_suppliers():
    df = suppliers_df()
    return df[df["risk_level"].isin(["High", "Critical"])].to_dict(orient="records")

def alternates_for(category: str):
    df = suppliers_df()
    hits = df[df["categories"].apply(lambda c: category in c)]
    return hits.sort_values("reliability_score", ascending=False).to_dict(orient="records")
