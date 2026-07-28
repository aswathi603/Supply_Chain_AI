"""
Unsupported Agent
"""
from langsmith import traceable

@traceable(name="Unsupported Agent")
def run(query: str) -> str:

    return f"""
⚠️ Sorry, I can't answer your question because it is outside my knowledge domain.

**Your Question**

> {query}

I am specifically designed for **Supply Chain Intelligence**.

I can help with topics such as:

- 🚚 Shipments
- 📦 Inventory
- 🏭 Suppliers
- 🏢 Warehouses
- 🚛 Logistics
- 📈 Forecasting
- 🛰️ Digital Twin Simulations
- 📊 Executive Reporting
- ⚠️ Risk Assessment
- 🔄 Recovery Planning

Please ask a question related to supply chain operations.
"""