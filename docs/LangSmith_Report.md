# LangSmith Integration Report

## Version

**v1.0.0**

---

# Overview

LangSmith is integrated into CrisisOps AI to provide observability, debugging, evaluation, and performance monitoring for the AI workflow.

It enables developers to trace every step of the AI pipeline, including agent execution, LangGraph workflows, LLM calls, prompts, tool usage, and response generation.

The integration helps developers understand how the system processes user requests and identify performance bottlenecks or reasoning errors.

---

# Objectives

The LangSmith integration aims to:

- Monitor AI workflow execution
- Trace agent interactions
- Debug prompt execution
- Measure LLM latency
- Analyze workflow performance
- Improve prompt quality
- Evaluate AI responses
- Simplify troubleshooting

---

# LangSmith Architecture

```
                 User
                  │
                  ▼
            Streamlit UI
                  │
                  ▼
          LangGraph Workflow
                  │
                  ▼
          Supervisor Agent
                  │
                  ▼
         Domain-Specific Agent
                  │
                  ▼
             Tool Layer
                  │
                  ▼
             API Layer
                  │
                  ▼
             LLM Request
                  │
                  ▼
             LangSmith SDK
                  │
                  ▼
         LangSmith Dashboard
```

---

# Configuration

The LangSmith configuration is stored in the `.env` file.

```env
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_api_key
LANGCHAIN_PROJECT=crisisops-ai
```

These environment variables enable tracing and connect the application to the appropriate LangSmith project.

---

# Project Configuration

The project contains a dedicated configuration module.

```
config/
└── langsmith_config.py
```

Responsibilities

- Load environment variables
- Enable tracing
- Initialize LangSmith client
- Manage project settings

---

# Traceable Components

The following components are instrumented using LangSmith.

## Supervisor Agent

Responsibilities

- Receives user query
- Determines target agent
- Starts workflow trace

---

## Shipment Agent

Tracks

- Prompt execution
- Tool usage
- LLM response generation

---

## Inventory Agent

Tracks

- Inventory retrieval
- Prompt construction
- Response generation

---

## Supplier Agent

Tracks

- Supplier lookup
- Risk analysis
- Recommendation generation

---

## Incident Agent

Tracks

- Incident analysis
- Impact evaluation
- AI reasoning

---

## Recovery Agent

Tracks

- Recovery planning
- Alternative recommendations
- Response generation

---

## Reporting Agent

Tracks

- KPI generation
- Report creation
- Executive summaries

---

## Forecasting Agent

Tracks

- Forecast request
- Prediction generation
- Business explanation

---

## Digital Twin Agent

Tracks

- Simulation request
- Scenario generation
- Impact analysis
- Recommendation generation

---

## Workflow Engine

Tracks

- Node execution
- Graph transitions
- Conditional routing
- Human approval flow

---

## Response Generator

Tracks

- Prompt
- Context
- LLM request
- Final output

---

# Trace Flow

```
User Query
      │
      ▼
Supervisor Agent
      │
      ▼
Selected Agent
      │
      ▼
Prompt Creation
      │
      ▼
Tool Execution
      │
      ▼
API Request
      │
      ▼
LLM Call
      │
      ▼
Response
      │
      ▼
LangSmith Trace
```

---

# Trace Information

Every trace records important execution details.

Examples include

- Trace ID
- Agent name
- Execution time
- Prompt
- Context
- Input
- Output
- Tool calls
- Errors
- Token usage
- Model name

---

# Benefits

LangSmith provides several advantages.

## Prompt Debugging

Developers can inspect the exact prompt sent to the LLM.

---

## Workflow Visibility

Shows every step executed within the LangGraph workflow.

---

## Agent Monitoring

Displays which agent handled each request and how it processed the task.

---

## Performance Monitoring

Measures

- Latency
- Execution time
- Token consumption

---

## Error Analysis

Identifies

- Failed tool calls
- Prompt errors
- Routing mistakes
- LLM failures

---

# Observability Workflow

```
User Request

↓

LangGraph

↓

Supervisor Agent

↓

Selected Agent

↓

Prompt

↓

LLM

↓

Trace Generated

↓

LangSmith Dashboard
```

---

# Metrics Monitored

The integration records several runtime metrics.

| Metric | Description |
|---------|-------------|
| Execution Time | Total processing time |
| Agent Name | Agent that handled the request |
| Prompt | Prompt sent to the LLM |
| Input | User query |
| Output | Generated response |
| Tool Calls | APIs and tools used |
| Token Usage | Number of input/output tokens |
| Errors | Exceptions during execution |
| Model | LLM used |
| Workflow Path | LangGraph execution path |

---

# Dashboard Features

The LangSmith dashboard provides:

- Trace history
- Workflow visualization
- Prompt inspection
- Token analysis
- Performance metrics
- Error tracking
- Execution timelines
- Project-level analytics

---

# Current Integration

The current implementation traces:

- Supervisor Agent
- Shipment Agent
- Inventory Agent
- Supplier Agent
- Incident Agent
- Recovery Agent
- Reporting Agent
- Forecasting Agent
- Digital Twin Agent
- LangGraph Workflow
- Response Generator

Tracing is implemented using the `@traceable` decorator.

Example

```python
from langsmith import traceable

@traceable(name="Shipment Agent")
def run(query):
    ...
```

---

# Future Enhancements

Future improvements include:

- Prompt version comparison
- Automated response evaluation
- Hallucination detection
- Cost monitoring
- Agent benchmarking
- Custom trace metadata
- User feedback integration
- Continuous AI quality monitoring

---

# Best Practices

To ensure reliable tracing:

- Enable tracing before starting the application.
- Restart the application after modifying environment variables.
- Use meaningful names in `@traceable` decorators.
- Trace all critical workflow components.
- Monitor execution regularly to detect failures early.

---

# Technology Stack

| Component | Technology |
|------------|------------|
| AI Framework | LangChain |
| Workflow Engine | LangGraph |
| Observability | LangSmith |
| LLM | Ollama / OpenAI |
| Frontend | Streamlit |
| Backend | Python |

---

# End-to-End Trace Flow

```
User

↓

Streamlit UI

↓

LangGraph Workflow

↓

Supervisor Agent

↓

Selected Agent

↓

Prompt Generation

↓

Tool Execution

↓

API Layer

↓

LLM

↓

LangSmith Trace

↓

Dashboard Visualization
```

---

# Summary

LangSmith provides comprehensive observability for CrisisOps AI by tracing every significant stage of the AI workflow. It enables developers to inspect prompts, monitor agent execution, evaluate workflow performance, analyze LLM interactions, and diagnose issues efficiently. The integration improves transparency, simplifies debugging, and supports the continuous optimization of the platform as it evolves into an enterprise-grade AI-powered Supply Chain Intelligence solution.