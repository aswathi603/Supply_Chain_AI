# Setup Guide

## Version

**v1.0.0**

---

# Overview

This guide explains how to configure and run the **CrisisOps AI** project in a local development environment.

The application is built using:

- Python
- Streamlit
- LangChain
- LangGraph
- Ollama
- LangSmith

Follow the steps below to install all dependencies and start the application successfully.

---

# System Requirements

## Operating System

- Windows 10 / 11
- Ubuntu 22.04+
- macOS 12+

---

## Software Requirements

| Software | Version |
|----------|----------|
| Python | 3.11 or above |
| Pip | Latest |
| Ollama | Latest |
| Git | Optional |
| VS Code | Recommended |

---

# Project Structure

Place the project folder anywhere on your local machine.

Example:

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
└── README.md
```

---

# Step 1: Open the Project

Open the project folder in your preferred code editor.

Example:

```
CrisisOps_AI
```

---

# Step 2: Open Terminal

Open a terminal inside the project directory.

Verify your current location.

```bash
pwd
```

or on Windows

```powershell
Get-Location
```

---

# Step 3: Create a Virtual Environment

### Windows

```bash
python -m venv myvenv
```

Activate it

```bash
myvenv\Scripts\activate
```

---

### Linux / macOS

```bash
python3 -m venv myvenv
```

Activate it

```bash
source myvenv/bin/activate
```

---

# Step 4: Install Required Packages

Install all dependencies listed in the project.

```bash
pip install -r requirements.txt
```

Wait until all packages are installed successfully.

---

# Step 5: Install Ollama

Download and install Ollama from the official website.

After installation, verify it is available.

```bash
ollama --version
```

---

# Step 6: Download Required Models

Download the language model used by the application.

```bash
ollama pull llama3.2:3b
```

Download the embedding model.

```bash
ollama pull embeddinggemma
```

Verify the models.

```bash
ollama list
```

Expected output:

```
llama3.2:3b

embeddinggemma
```

---

# Step 7: Create Environment File

Inside the project root, create a file named

```
.env
```

Add the following configuration.

```env
LLM_PROVIDER=ollama

OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2:3b
OLLAMA_EMBEDDING_MODEL=embeddinggemma

LLM_TEMPERATURE=0.2

LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=<YOUR_LANGSMITH_API_KEY>
LANGCHAIN_PROJECT=crisisops-ai
```

Replace `<YOUR_LANGSMITH_API_KEY>` with your own LangSmith API key.

---

# Step 8: Start Ollama

Ensure the Ollama server is running.

```bash
ollama serve
```

If it is already running, you can skip this step.

---

# Step 9: Launch the Application

Run the Streamlit application.

```bash
streamlit run app.py
```

After a few seconds, the terminal will display:

```
Local URL:
http://localhost:8501
```

Open the URL in your web browser.

---

# Verify the Installation

## Verify Python

```bash
python --version
```

---

## Verify Installed Packages

```bash
pip list
```

---

## Verify Ollama

```bash
ollama list
```

---

## Verify Environment Variables

Run Python.

```bash
python
```

Execute:

```python
import os
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("LANGCHAIN_TRACING_V2"))
print(os.getenv("LANGCHAIN_PROJECT"))
```

Expected output:

```
true

crisisops-ai
```

---

# Running the Application

Once the application starts successfully, you can:

- Ask supply chain-related questions
- View shipment information
- Analyze inventory
- Generate reports
- Run forecasting
- Perform Digital Twin simulations
- View AI-generated recommendations

---

# Application Startup Flow

```
Start Application

↓

Load Environment Variables

↓

Load Configuration

↓

Initialize LangGraph

↓

Initialize Agents

↓

Initialize Memory

↓

Initialize Streamlit

↓

Application Ready
```

---

# Common Troubleshooting

## Virtual Environment Not Activated

Activate the environment.

Windows

```bash
myvenv\Scripts\activate
```

Linux/macOS

```bash
source myvenv/bin/activate
```

---

## Missing Packages

Reinstall all dependencies.

```bash
pip install -r requirements.txt
```

---

## Ollama Connection Error

Start the Ollama server.

```bash
ollama serve
```

Verify downloaded models.

```bash
ollama list
```

---

## LangSmith Traces Not Appearing

Verify the following in the `.env` file.

```env
LANGCHAIN_TRACING_V2=true
```

Restart the application after updating the file.

---

## Port Already in Use

Run the application on another port.

```bash
streamlit run app.py --server.port 8502
```

---

# Updating Dependencies

To update all installed packages.

```bash
pip install --upgrade -r requirements.txt
```

---

# Running Tests

Run all tests.

```bash
pytest
```

Run a specific test.

```bash
pytest tests/
```

---

# Recommended Development Tools

| Tool | Purpose |
|------|----------|
| VS Code | Source Code Editor |
| Python | Backend Development |
| Streamlit | User Interface |
| Ollama | Local LLM |
| LangChain | AI Framework |
| LangGraph | Workflow Orchestration |
| LangSmith | Observability |
| Git | Version Control |

---

# Setup Checklist

- Project folder is available locally
- Python is installed
- Virtual environment created
- Virtual environment activated
- Dependencies installed
- Ollama installed
- Required models downloaded
- `.env` file created
- LangSmith configured
- Ollama server running
- Streamlit application started successfully

---

# Conclusion

The CrisisOps AI project is now configured and ready to use. Once the application is running, users can interact with multiple AI agents to monitor supply chain operations, analyze disruptions, perform Digital Twin simulations, generate forecasts, and receive AI-powered business recommendations through an interactive Streamlit interface.