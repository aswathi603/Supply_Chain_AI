"""
Memory Utilities

Helper functions for working with conversation history.
"""

from typing import List, Dict


def format_history(history: List[Dict]) -> str:
    """
    Convert chat history into a readable text block
    for the LLM prompt.
    """

    if not history:
        return ""

    lines = []

    for message in history:

        role = message.get("role", "unknown").title()

        content = message.get("content", "")

        lines.append(
            f"{role}: {content}"
        )

    return "\n".join(lines)


def trim_history(
    history: List[Dict],
    max_messages: int = 10,
) -> List[Dict]:
    """
    Keep only the most recent messages.
    """

    return history[-max_messages:]


def last_user_message(
    history: List[Dict],
) -> str:
    """
    Return the latest user message.
    """

    for message in reversed(history):

        if message.get("role") == "user":

            return message.get("content", "")

    return ""


def count_messages(
    history: List[Dict],
) -> int:
    """
    Return total messages.
    """

    return len(history)