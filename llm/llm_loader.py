"""
LLM Loader.

Loads the configured provider.
"""

from langchain_ollama import ChatOllama

from config.settings import (
    LLM_PROVIDER,
    LLM_TEMPERATURE,
    OLLAMA_BASE_URL,
    OLLAMA_MODEL,
    OPENAI_API_KEY,
    OPENAI_MODEL,
)


def get_llm():

    if LLM_PROVIDER == "ollama":

        return ChatOllama(
            model=OLLAMA_MODEL,
            temperature=LLM_TEMPERATURE,
            base_url=OLLAMA_BASE_URL,
        )

    if LLM_PROVIDER == "openai":

        if not OPENAI_API_KEY:
            return None

        from langchain_openai import ChatOpenAI

        return ChatOpenAI(
            model=OPENAI_MODEL,
            api_key=OPENAI_API_KEY,
            temperature=LLM_TEMPERATURE,
        )

    return None