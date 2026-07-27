# Architecture

```
Streamlit UI  →  LangGraph Workflow  →  Supervisor  →  Specialist Agents
                                                    ↘  Tools  →  Services  →  Mock JSON API
                                                    ↘  Digital Twin  →  Simulations
```

- **Agents:** Supervisor, Shipment, Inventory, Supplier, Incident, Recovery, Reporting, Digital Twin
- **Graph:** `graph/graph_builder.py` builds a LangGraph StateGraph (supervisor → agent → END).
  Falls back to plain function call if `langgraph` isn't installed.
- **Data:** All entities live in `/data/*.json`. Loaded via `utils/json_loader.py`.
