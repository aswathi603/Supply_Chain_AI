"""
Graph Logger

Provides lightweight logging utilities for the LangGraph workflow.
"""

import logging
from datetime import datetime
from pathlib import Path

# ==========================================================
# Log Directory
# ==========================================================

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "graph.log"

# ==========================================================
# Logger Configuration
# ==========================================================

logger = logging.getLogger("CrisisOpsGraph")

if not logger.handlers:

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8",
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)


# ==========================================================
# Helper Functions
# ==========================================================

def log_event(
    node: str,
    message: str,
):
    """
    Log a workflow event.
    """

    logger.info(
        f"[{node}] {message}"
    )


def log_query(
    query: str,
):
    """
    Log incoming user query.
    """

    logger.info(
        f"[QUERY] {query}"
    )


def log_route(
    route: str,
):
    """
    Log supervisor routing decision.
    """

    logger.info(
        f"[ROUTE] {route}"
    )


def log_agent(
    agent: str,
):
    """
    Log agent execution.
    """

    logger.info(
        f"[AGENT] {agent}"
    )


def log_error(
    error: Exception,
):
    """
    Log exceptions.
    """

    logger.exception(error)


def log_completion():
    """
    Log successful workflow completion.
    """

    logger.info(
        "[WORKFLOW COMPLETED]"
    )