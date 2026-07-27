"""
Embedding loader.
Uses Ollama embedding model.
"""

from langchain_ollama import OllamaEmbeddings

from config.settings import (
    OLLAMA_BASE_URL,
    OLLAMA_EMBEDDING_MODEL,
)

_embedding = OllamaEmbeddings(
    model=OLLAMA_EMBEDDING_MODEL,
    base_url=OLLAMA_BASE_URL,
)


def embed(texts: list[str]) -> list[list[float]]:
    """
    Generate embeddings.

    Args:
        texts: List of text strings.

    Returns:
        List of embedding vectors.
    """
    return _embedding.embed_documents(texts)