# CrisisOps AI — Supply Chain

A **multi-agent supply chain intelligence platform** built with Streamlit + LangGraph.

## Features
- 📊 Interactive dashboard (KPIs, live shipment map, inventory heatmap)
- 💬 Chat with a multi-agent supervisor (Shipment, Inventory, Supplier, Incident, Recovery agents)
- 🧪 Digital-twin simulations (rerouting, supplier replacement, demand spikes, etc.)
- 📈 Forecasting (demand, delays, warehouse utilization)
- 🗂 Mock JSON data — runs out-of-the-box

## Quick Start (Local VSCode)

```bash
cd SupplyChainAI
python -m venv venv
source venv/bin/activate      # windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env .env.local            # optional
# add your OPENAI_API_KEY inside .env
streamlit run app.py
```

Open http://localhost:8501

## Environment Variables

| Key | Purpose |
|-----|---------|
| `OPENAI_API_KEY` | OpenAI key (default provider) |
| `ANTHROPIC_API_KEY` | Optional — Claude |
| `GOOGLE_API_KEY` | Optional — Gemini |
| `LLM_PROVIDER` | `openai` \| `anthropic` \| `google` |
| `LLM_MODEL` | e.g. `gpt-4o-mini` |

> The app runs in **demo mode** without an LLM key — agent replies use rule-based mock reasoning so the dashboard and simulations still work.

## Deploy to Streamlit Cloud

1. Push this folder to GitHub
2. On [share.streamlit.io](https://share.streamlit.io), create app → point to `app.py`
3. Set secrets (Settings → Secrets):
   ```
   OPENAI_API_KEY = "sk-..."
   ```

## Structure

See folder tree in `docs/Architecture.md`.
