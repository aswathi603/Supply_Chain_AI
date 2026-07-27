"""LangSmith configuration."""

import os
from dotenv import load_dotenv

load_dotenv()

LANGSMITH_ENABLED = (
    os.getenv("LANGCHAIN_TRACING_V2", "false").lower() == "true"
)

LANGSMITH_API_KEY = os.getenv("LANGCHAIN_API_KEY", "")

LANGSMITH_PROJECT = os.getenv(
    "LANGCHAIN_PROJECT",
    "CrisisOpsAI",
)