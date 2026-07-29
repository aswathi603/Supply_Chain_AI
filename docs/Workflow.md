# Workflow

## Version

**v1.0.0**

---

# Overview

This document describes the complete workflow of the **CrisisOps AI** platform.

The application follows a **LangGraph-based Multi-Agent Workflow**, where a user's request is routed through a supervisor agent to specialized AI agents that retrieve business data, interact with the Large Language Model (LLM), and generate intelligent responses.

---

# Overall Workflow

```
                User
                  │
                  ▼
        Streamlit User Interface
                  │
                  ▼
          LangGraph Workflow
                  │
                  ▼
         Supervisor Agent
                  │
                  ▼
               Router
                  │
        ┌─────────┼─────────┐
        │         │         │
        ▼         ▼         ▼
   Shipment   Inventory   Supplier
     Agent       Agent      Agent
        │         │         │
        ├─────────┼─────────┤
                  ▼
          Incident Agent
                  │
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
            JSON Data Files
                  │
                  ▼
          LLM (Ollama/OpenAI)
                  │
                  ▼
         AI Generated Response
                  │
                  ▼
      Conversation Memory Update
                  │
                  ▼
        Streamlit User Interface
```

---

# Request Processing Workflow

Every user query follows the same execution flow.

```
User enters a query

↓

Streamlit receives the request

↓

LangGraph starts execution

↓

Supervisor Agent analyzes the request

↓

Router determines the correct agent

↓

Selected agent builds context

↓

Conversation history is retrieved

↓

Tool layer retrieves business data

↓

API loads required datasets

↓

Prompt is generated

↓

LLM processes the prompt

↓

AI response is generated

↓

Conversation memory is updated

↓

Response displayed to the user
```

---

# Workflow Components

## Step 1 - User Interaction

The user submits a supply chain-related query through the Streamlit interface.

Examples

- Show delayed shipments
- Find low inventory products
- Predict next month's demand
- Simulate supplier failure
- Generate executive report

---

## Step 2 - Streamlit UI

The Streamlit application

- Accepts the query
- Displays chat history
- Shows dashboards
- Displays KPIs
- Renders AI responses

---

## Step 3 - LangGraph Workflow

LangGraph acts as the workflow orchestrator.

Responsibilities

- Execute nodes
- Control workflow
- Route requests
- Handle human approval
- Maintain execution state

---

## Step 4 - Supervisor Agent

The Supervisor Agent is the central controller.

Responsibilities

- Receive user query
- Understand intent
- Select the appropriate specialist agent
- Forward the request

---

## Step 5 - Router

The Router classifies the request into one of the supported domains.

Supported routes

- Shipment
- Inventory
- Supplier
- Incident
- Recovery
- Reporting
- Forecasting
- Digital Twin
- Unsupported

If a query is outside the supported domain, it is routed to the Unsupported Agent.

---

## Step 6 - Domain Agent

The selected AI agent

- Builds the prompt
- Retrieves memory
- Calls tools
- Generates the response

Each agent specializes in a specific business area.

---

# Agent Workflow

```
Receive Query

↓

Load Conversation Context

↓

Retrieve Business Data

↓

Build Prompt

↓

Call LLM

↓

Generate Response

↓

Return Result
```

---

# Tool Workflow

The Tool Layer acts as the bridge between agents and the API layer.

```
Agent

↓

Tool Function

↓

API

↓

Dataset

↓

Structured Data
```

Responsibilities

- Retrieve business data
- Format records
- Filter information
- Return structured results

---

# API Workflow

The API layer accesses the required datasets.

```
API Request

↓

Load JSON

↓

Validate Data

↓

Filter Records

↓

Return Results
```

The API layer contains no business logic.

---

# Data Workflow

The project currently uses JSON files as the primary data source.

```
JSON Files

↓

Mock Loader

↓

API

↓

Tools

↓

Agents
```

Datasets include

- Shipments
- Inventory
- Suppliers
- Warehouses
- Orders
- Customers
- Transportation
- Incidents
- Demand

---

# LLM Workflow

The LLM generates natural language responses.

```
Agent Prompt

↓

Context

↓

Business Data

↓

LLM

↓

Generated Response
```

Supported providers

- Ollama
- OpenAI

---

# Memory Workflow

Conversation history improves contextual understanding.

```
User Query

↓

Memory Manager

↓

Conversation History

↓

Context Builder

↓

Prompt

↓

LLM

↓

Store New Conversation
```

Features

- Multiple chats
- Chat history
- Conversation summaries
- Context retrieval

---

# Forecasting Workflow

```
Historical Data

↓

Forecasting Agent

↓

Prediction Model

↓

Business Analysis

↓

Visualization
```

Supports

- Demand forecasting
- Delay prediction
- Inventory forecasting

---

# Digital Twin Workflow

```
Simulation Request

↓

Current State Builder

↓

Scenario Generator

↓

Simulation Engine

↓

Business Rules

↓

Impact Analysis

↓

Recommendations

↓

Confidence Score

↓

Response
```

Supports simulations such as

- Shipment rerouting
- Supplier replacement
- Inventory redistribution
- Warehouse optimization

---

# Reporting Workflow

```
Business Data

↓

Reporting Agent

↓

KPI Generation

↓

Summary Creation

↓

Executive Report
```

Reports may include

- Shipment summary
- Inventory status
- Supplier performance
- Incident analysis

---

# Human Approval Workflow

Certain operations can require manual approval.

```
Agent Recommendation

↓

Approval Required?

↓

Yes

↓

Human Review

↓

Approve / Reject

↓

Continue Workflow
```

---

# LangSmith Workflow

LangSmith monitors AI execution.

```
Workflow Execution

↓

Trace Generation

↓

Prompt Logging

↓

Tool Logging

↓

Performance Metrics

↓

LangSmith Dashboard
```

Tracks

- Prompt execution
- Agent performance
- Tool usage
- LLM latency
- Errors

---

# Error Handling Workflow

```
User Request

↓

Workflow Execution

↓

Exception?

↓

Yes

↓

Log Error

↓

Return Friendly Message

↓

Continue Application
```

Examples

- Missing dataset
- Invalid query
- API failure
- LLM failure

---

# End-to-End Execution Flow

```
User

↓

Streamlit

↓

LangGraph

↓

Supervisor Agent

↓

Router

↓

Domain Agent

↓

Memory

↓

Tool Layer

↓

API Layer

↓

JSON Data

↓

LLM

↓

Generate Response

↓

Memory Update

↓

LangSmith Trace

↓

Display Response
```

---

# Workflow Summary

| Stage | Component | Responsibility |
|--------|-----------|----------------|
| 1 | Streamlit UI | Receive user input |
| 2 | LangGraph | Execute workflow |
| 3 | Supervisor Agent | Analyze query |
| 4 | Router | Select appropriate agent |
| 5 | Domain Agent | Process request |
| 6 | Memory | Retrieve conversation history |
| 7 | Tool Layer | Access business data |
| 8 | API Layer | Load datasets |
| 9 | LLM | Generate AI response |
| 10 | LangSmith | Trace execution |
| 11 | Streamlit UI | Display results |

---

# Key Characteristics

The workflow is designed with the following principles:

- Multi-Agent Architecture
- Modular Components
- Layered Design
- Intelligent Query Routing
- Context-Aware Conversations
- Reusable Services
- Human-in-the-Loop Support
- AI Observability with LangSmith
- Extensible Business Logic
- Scalable Workflow Execution

---

# Conclusion

The CrisisOps AI workflow combines LangGraph orchestration, specialized AI agents, structured business data, and Large Language Models to deliver intelligent supply chain insights. Each user request follows a well-defined execution path, ensuring accurate routing, contextual understanding, efficient data retrieval, and transparent AI processing. This modular workflow allows the platform to scale easily while supporting future enhancements such as real-time integrations, advanced analytics, and autonomous decision-making.