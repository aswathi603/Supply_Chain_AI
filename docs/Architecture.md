# CrisisOps AI Architecture

## Version

**v1.0.0**

---

# Overview

CrisisOps AI is a Multi-Agent Supply Chain Intelligence Platform that leverages Artificial Intelligence, Large Language Models (LLMs), LangGraph workflows, Digital Twin simulations, and Predictive Analytics to assist supply chain managers in monitoring operations, forecasting disruptions, simulating recovery strategies, and generating intelligent business recommendations.

The application follows a **Layered Multi-Agent Architecture**, where each layer has a dedicated responsibility, ensuring modularity, maintainability, scalability, and extensibility.

---

# System Architecture

```
                           User
                             │
                             ▼
                    Streamlit User Interface
                             │
                             ▼
                     LangGraph Workflow Engine
                             │
                             ▼
                     Supervisor Agent (Router)
                             │
 ┌─────────────┬──────────────┼──────────────┬─────────────┐
 │             │              │              │             │
 ▼             ▼              ▼              ▼             ▼
Shipment   Inventory     Supplier      Incident     Reporting
 Agent       Agent         Agent          Agent        Agent
 │             │              │              │             │
 └───────┬─────┴──────┬───────┴──────────────┴─────────────┘
         ▼
 Recovery Agent
         │
         ▼
 Forecasting Agent
         │
         ▼
 Digital Twin Agent
         │
         ▼
      Tool Layer
         │
         ▼
      API Layer
         │
         ▼
 JSON Data Sources
         │
         ▼
     LLM (Ollama/OpenAI)
         │
         ▼
 Streamlit Dashboard
```

---

# Architecture Layers

The application is divided into multiple logical layers.

```
Presentation Layer

↓

Workflow Layer

↓

Agent Layer

↓

Tool Layer

↓

API Layer

↓

Data Layer

↓

LLM Layer

↓

Memory Layer

↓

Logging & Observability
```

---

# Project Folder Structure

```
CrisisOps_AI/

├── agents/
├── api/
├── assets/
├── config/
├── data/
├── digital_twin/
├── docs/
├── evaluation/
├── forecasting/
├── graph/
├── llm/
├── logs/
├── memory/
├── models/
├── prompts/
├── services/
├── simulations/
├── tests/
├── tools/
├── ui/
├── utils/
│
├── app.py
├── requirements.txt
├── README.md
└── .env
```

---

# Folder Responsibilities

---

## 1. app.py

### Purpose

Application entry point.

### Responsibilities

- Initialize Streamlit
- Load configuration
- Load CSS
- Render Header
- Render Sidebar
- Navigate between pages
- Initialize Memory
- Handle application exceptions

Workflow

```
Start Application

↓

Load Configuration

↓

Load CSS

↓

Initialize Session

↓

Render Header

↓

Render Sidebar

↓

Open Selected Page
```

---

## 2. ui/

### Purpose

Presentation layer of the application.

Contains

- Dashboard
- Chat Interface
- Forecasting Dashboard
- Simulation Dashboard
- Sidebar
- Components

Responsibilities

- Render UI
- Accept user input
- Display AI responses
- Display charts
- Display KPIs

---

## 3. graph/

### Purpose

Workflow orchestration using LangGraph.

Contains

```
workflow.py

↓

graph_builder.py

↓

nodes.py

↓

conditional_edges.py

↓

human_approval.py
```

Responsibilities

- Build workflow
- Route execution
- Handle approval
- Execute agents

Workflow

```
User Query

↓

Supervisor Node

↓

Agent Node

↓

Approval (Optional)

↓

End
```

---

## 4. agents/

Contains domain-specific AI agents.

```
Supervisor Agent

↓

Router

↓

Shipment Agent

Inventory Agent

Supplier Agent

Incident Agent

Recovery Agent

Reporting Agent

Forecasting Agent

Digital Twin Agent

Unsupported Agent
```

Responsibilities

- Build context
- Call tools
- Execute LLM
- Generate responses

---

## 5. prompts/

Stores system prompts for every AI agent.

```
shipment_prompt.py

inventory_prompt.py

supplier_prompt.py

incident_prompt.py

recovery_prompt.py

reporting_prompt.py

forecasting_prompt.py

digital_twin_prompt.py

system_prompt.py
```

Each agent uses its own prompt for domain-specific reasoning.

---

## 6. tools/

Acts as the bridge between agents and APIs.

Responsibilities

- Data retrieval
- Business calculations
- Data formatting

Workflow

```
Agent

↓

Tool

↓

API
```

---

## 7. api/

Provides structured access to business data.

Contains

```
Shipment API

Inventory API

Supplier API

Warehouse API

Incident API

Order API

Transportation API

Mock Loader
```

Responsibilities

- Load JSON
- Filter records
- Return structured data

---

## 8. data/

Stores business datasets.

Examples

```
shipments.json

inventory.json

suppliers.json

warehouses.json

orders.json

customers.json

incidents.json

transportation.json

demand.json
```

---

## 9. services/

Contains business logic.

Examples

```
Shipment Service

Inventory Service

Supplier Service

Forecasting Service

Reporting Service

Digital Twin Service
```

Responsibilities

- KPI calculation
- Report generation
- Recovery planning
- Simulation orchestration

---

## 10. digital_twin/

Implements Digital Twin simulations.

Modules

```
Scenario Generator

↓

State Builder

↓

Simulation Engine

↓

Business Rules

↓

Impact Analyzer

↓

Recommendation Engine

↓

Confidence Engine
```

---

## 11. forecasting/

Implements predictive analytics.

Capabilities

- Demand Forecast
- Delay Prediction
- Warehouse Utilization
- Business Impact
- Capacity Forecast

Workflow

```
Historical Data

↓

Forecast Model

↓

Prediction

↓

Dashboard
```

---

## 12. llm/

Responsible for LLM communication.

Workflow

```
Agent

↓

Prompt

↓

Context

↓

LLM Loader

↓

Ollama/OpenAI

↓

Output Parser

↓

Response
```

Supports

- Ollama
- OpenAI

---

## 13. memory/

Conversation memory subsystem.

Components

```
Chat History

↓

Memory Manager

↓

Conversation Summary

↓

Context Builder
```

Responsibilities

- Store conversations
- Retrieve history
- Build conversational context
- Support multiple chats

---

## 14. models/

Defines business entities.

Examples

- Shipment
- Supplier
- Warehouse
- Inventory
- Order
- Incident

---

## 15. simulations/

Contains independent simulation algorithms.

Supported simulations

- Shipment Rerouting
- Supplier Replacement
- Demand Spike
- Warehouse Capacity
- Inventory Redistribution
- Transportation Comparison
- Customs Delay

---

## 16. config/

Application configuration.

Contains

- Environment variables
- LLM configuration
- LangSmith configuration
- Constants

---

## 17. utils/

Shared helper utilities.

Examples

- Logger
- Formatter
- Visualization
- Validators
- Helper functions

---

## 18. assets/

Stores UI resources.

```
styles.css
```

---

## 19. logs/

Stores application logs.

Examples

```
graph.log

application.log
```

---

## 20. evaluation/

Used for AI evaluation.

Supports

- Prompt testing
- Agent benchmarking
- Performance analysis
- LangSmith tracing

---

## 21. tests/

Contains automated tests.

Examples

- Unit Tests
- Integration Tests
- Workflow Tests
- Simulation Tests

---

## 22. docs/

Contains project documentation.

Examples

- Architecture.md
- API_Documentation.md
- Digital_Twin_Design.md
- Future_Enhancements.md
- Workflow.md

---

# End-to-End Workflow

```
User

↓

Streamlit UI

↓

LangGraph Workflow

↓

Supervisor Agent

↓

Router

↓

Selected Agent

↓

Build Context

↓

Conversation Memory

↓

Tool Layer

↓

API Layer

↓

JSON Data

↓

LLM (Ollama/OpenAI)

↓

Generated Response

↓

Conversation Memory Updated

↓

Streamlit Dashboard
```

---

# Agent Workflow

```
User Query

↓

Supervisor Agent

↓

Router

↓

Select Agent

↓

Build Context

↓

Execute Tools

↓

Generate Prompt

↓

LLM

↓

Business Response
```

---

# Forecasting Workflow

```
Historical Data

↓

Forecasting Service

↓

Prediction

↓

Business Impact

↓

Dashboard Visualization
```

---

# Digital Twin Workflow

```
Simulation Request

↓

Scenario Generator

↓

Current State Builder

↓

Simulation Engine

↓

Business Rules

↓

Impact Analyzer

↓

Recommendation Engine

↓

Confidence Engine

↓

Dashboard
```

---

# Memory Workflow

```
User Message

↓

Memory Manager

↓

Conversation History

↓

Context Builder

↓

Agent

↓

LLM

↓

Assistant Response

↓

Memory Updated
```

---

# Technology Stack

| Layer | Technology |
|--------|------------|
| Frontend | Streamlit |
| Backend | Python |
| Workflow Engine | LangGraph |
| AI Framework | LangChain |
| LLM | Ollama / OpenAI |
| Observability | LangSmith |
| Simulation | Custom Digital Twin Engine |
| Forecasting | Python Predictive Models |
| Storage | JSON Files |
| Styling | CSS |

---

# Design Principles

The architecture is based on the following principles:

- Layered Architecture
- Multi-Agent Design
- Separation of Concerns
- Modular Components
- Reusable Services
- Scalable Workflow
- Explainable AI
- Human-in-the-Loop Support
- Extensible Agent Framework
- Maintainable Code Structure

---

# Key Features

- Multi-Agent AI Architecture
- LangGraph Workflow Orchestration
- Domain-Specific AI Agents
- Supply Chain Analytics
- Predictive Forecasting
- Digital Twin Simulations
- AI-Powered Recommendations
- Multiple Conversation Support
- Human Approval Workflow
- LangSmith Observability
- Modular API Layer
- Business KPI Dashboard

---

# Architecture Summary

CrisisOps AI follows a modular, layered, and agent-oriented architecture. User interactions begin in the Streamlit interface and are orchestrated through LangGraph, where the Supervisor Agent routes requests to specialized domain agents. These agents build context using conversation memory, retrieve business data through tools and APIs, and generate intelligent responses using Large Language Models. Supporting modules such as Forecasting, Digital Twin Simulation, and Reporting extend the platform with predictive and analytical capabilities, while LangSmith provides observability for tracing and debugging. This architecture ensures scalability, maintainability, and readiness for future enterprise integrations.