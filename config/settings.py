"""
Global application settings.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

ENV_PATH = Path(__file__).resolve().parent.parent / ".env"

print("Loading .env from:", ENV_PATH)

load_dotenv(
    dotenv_path=ENV_PATH,
    override=True,
)

# ============================================================
# Application
# ============================================================

APP_NAME = "CrisisOps AI"

APP_TAGLINE = (
    "Multi-Agent Supply Chain Intelligence & Digital Twin Platform"
)

APP_ICON = "🛰️"

ROOT_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = ROOT_DIR / "data"

# ============================================================
# Provider
# ============================================================

LLM_PROVIDER = os.getenv(
    "LLM_PROVIDER",
    "ollama",
).lower()

LLM_TEMPERATURE = float(
    os.getenv(
        "LLM_TEMPERATURE",
        "0.2",
    )
)

# ============================================================
# Ollama
# ============================================================

OLLAMA_BASE_URL = os.getenv(
    "OLLAMA_BASE_URL",
    "http://localhost:11434",
)

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "llama3.2:3b",
)

OLLAMA_EMBEDDING_MODEL = os.getenv(
    "OLLAMA_EMBEDDING_MODEL",
    "embeddinggemma",
)

# ============================================================
# OpenAI (Optional)
# ============================================================

OPENAI_API_KEY = os.getenv(
    "OPENAI_API_KEY",
    "",
)

OPENAI_MODEL = os.getenv(
    "OPENAI_MODEL",
    "gpt-4o-mini",
)

# ============================================================
# Optional Providers
# ============================================================

ANTHROPIC_API_KEY = os.getenv(
    "ANTHROPIC_API_KEY",
    "",
)

GOOGLE_API_KEY = os.getenv(
    "GOOGLE_API_KEY",
    "",
)

# ============================================================
# Runtime Flags
# ============================================================

HAS_OLLAMA = LLM_PROVIDER == "ollama"

HAS_OPENAI = bool(OPENAI_API_KEY)

HAS_LLM = HAS_OLLAMA or HAS_OPENAI

# ============================================================
# Backward Compatibility
# ============================================================

HAS_LLM_KEY = HAS_LLM