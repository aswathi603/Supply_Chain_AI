"""LLM configuration."""

from config.settings import (
    LLM_PROVIDER,
    LLM_TEMPERATURE,
    OLLAMA_MODEL,
    OPENAI_MODEL,
)

LLM_SETTINGS = {
    "provider": LLM_PROVIDER,
    "temperature": LLM_TEMPERATURE,
    "max_tokens": 800,
    "models": {
        "ollama": OLLAMA_MODEL,
        "openai": OPENAI_MODEL,
    },
}