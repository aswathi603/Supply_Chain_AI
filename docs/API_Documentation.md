# CrisisOps AI - API Documentation

## Version

**v1.0.0**

---

# Overview

The API layer acts as the data access layer of CrisisOps AI.

It abstracts the underlying JSON datasets and provides clean interfaces for agents and tools to retrieve supply chain information.

The API layer does **not** contain business logic.

Its only responsibility is to:

- Load data
- Filter records
- Return structured information
- Hide implementation details from agents

---

# API Architecture

```
JSON Files
     │
     ▼
API Layer
     │
     ▼
Tools Layer
     │
     ▼
Agents
```

---

# Folder Structure

```
api/

├── __init__.py
├── base_api.py
├── mock_loader.py
├── shipment_api.py
├── inventory_api.py
├── supplier_api.py
├── warehouse_api.py
├── transportation_api.py
├── incident_api.py
└── order_api.py
```

---

# API Workflow

```
User Query
      │
      ▼
Selected Agent
      │
      ▼
Tool Function
      │
      ▼
API Function
      │
      ▼
JSON Dataset
      │
      ▼
Structured Data
      │
      ▼
LLM Response
```

---

# Base API

## File

```
api/base_api.py
```

## Purpose

Provides common helper functions used by every API.

### Responsibilities

- Load datasets
- Validate records
- Handle exceptions
- Return standardized responses

---

# Mock Loader

## File

```
api/mock_loader.py
```

## Purpose

Loads JSON datasets from the **data/** directory.

### Data Source

```
data/
```

Supported datasets

- shipments.json
- inventory.json
- suppliers.json
- warehouses.json
- incidents.json
- transportation.json
- orders.json
- customers.json
- routes.json
- demand.json

---

# Shipment API

## File

```
shipment_api.py
```

## Description

Provides shipment-related information.

### Data Source

```
shipments.json
```

### Typical Operations

- Load shipments
- Get delayed shipments
- Get shipment status
- Retrieve shipment by ID
- List shipments in transit
- List cancelled shipments
- Get customs shipments

### Used By

- Shipment Agent
- Reporting Agent
- Recovery Agent
- Digital Twin Agent

---

# Inventory API

## File

```
inventory_api.py
```

## Description

Provides inventory information.

### Data Source

```
inventory.json
```

### Typical Operations

- Retrieve inventory
- Low stock products
- Reorder information
- Warehouse inventory
- SKU lookup
- Inventory valuation

### Used By

- Inventory Agent
- Forecasting Agent
- Reporting Agent

---

# Supplier API

## File

```
supplier_api.py
```

## Description

Provides supplier information.

### Data Source

```
suppliers.json
```

### Typical Operations

- Supplier lookup
- Reliability score
- Lead time
- Supplier ranking
- Alternate suppliers

### Used By

- Supplier Agent
- Recovery Agent
- Reporting Agent

---

# Warehouse API

## File

```
warehouse_api.py
```

## Description

Provides warehouse information.

### Data Source

```
warehouses.json
```

### Typical Operations

- Warehouse capacity
- Inventory levels
- Warehouse utilization
- Storage information

### Used By

- Inventory Agent
- Digital Twin Agent
- Forecasting Agent

---

# Transportation API

## File

```
transportation_api.py
```

## Description

Provides transportation information.

### Data Source

```
transportation.json
```

### Typical Operations

- Transportation routes
- Transportation cost
- Carrier information
- Air vs Ocean comparison
- ETA lookup

### Used By

- Shipment Agent
- Forecasting Agent
- Digital Twin Agent

---

# Incident API

## File

```
incident_api.py
```

## Description

Provides disruption and incident information.

### Data Source

```
incidents.json
```

### Typical Operations

- Open incidents
- Critical incidents
- Risk assessment
- Shipment impact
- Incident summary

### Used By

- Incident Agent
- Recovery Agent
- Reporting Agent

---

# Order API

## File

```
order_api.py
```

## Description

Provides customer order information.

### Data Source

```
orders.json
```

### Typical Operations

- Order lookup
- Order status
- Customer orders
- Pending orders
- Completed orders

### Used By

- Reporting Agent
- Shipment Agent

---

# Data Flow

```
shipments.json
inventory.json
suppliers.json
warehouses.json
orders.json
incidents.json
transportation.json

        │
        ▼

Mock Loader

        │
        ▼

Specific API

        │
        ▼

Tool Layer

        │
        ▼

Agent

        │
        ▼

LLM
```

---

# API Dependencies

```
Agents
   │
   ▼
Tools
   │
   ▼
API Layer
   │
   ▼
Mock Loader
   │
   ▼
JSON Files
```

---

# Error Handling

Every API follows a consistent error handling strategy.

### Possible Errors

- Dataset not found
- Invalid JSON
- Missing record
- Invalid ID
- Empty dataset

Example

```python
try:
    data = load_shipments()
except Exception:
    return []
```

---

# Design Principles

The API layer follows these principles:

- Single Responsibility Principle
- Separation of Concerns
- Read-Only Data Access
- Reusable Functions
- Lightweight Processing
- Easy to Replace with Real REST APIs

---

# Future Enhancements

The current implementation reads from local JSON files.

Future versions can replace the API layer with:

- REST APIs
- FastAPI
- GraphQL
- PostgreSQL
- MongoDB
- SAP APIs
- Oracle SCM APIs
- Azure Supply Chain APIs

Since agents only communicate with the API layer, replacing the backend data source will not require changes to the agents.

---

# API Summary

| API | Dataset | Primary Consumer |
|------|----------|------------------|
| Shipment API | shipments.json | Shipment Agent |
| Inventory API | inventory.json | Inventory Agent |
| Supplier API | suppliers.json | Supplier Agent |
| Warehouse API | warehouses.json | Inventory Agent |
| Transportation API | transportation.json | Shipment Agent |
| Incident API | incidents.json | Incident Agent |
| Order API | orders.json | Reporting Agent |
| Mock Loader | All JSON Files | All APIs |
| Base API | Shared Utilities | All APIs |

---

# Complete API Flow

```
User
 │
 ▼
Supervisor Agent
 │
 ▼
Domain Agent
 │
 ▼
Tool Function
 │
 ▼
API Layer
 │
 ▼
Mock Loader
 │
 ▼
JSON Dataset
 │
 ▼
Structured Data
 │
 ▼
LLM
 │
 ▼
Business Response
 │
 ▼
Streamlit UI
```

---

# Conclusion

The API layer provides a clean abstraction between the business logic and the underlying datasets. By isolating data access into dedicated API modules, CrisisOps AI remains modular, maintainable, and easily extensible for future integration with enterprise databases or live supply chain systems.