"""
Conversation Memory
"""

from datetime import datetime

from memory.memory_manager import memory


def remember_user(text: str):

    memory.add(
        "user",
        text,
        time=datetime.now().strftime("%H:%M:%S"),
    )


def remember_assistant(
    text: str,
    agent=None,
):

    memory.add(
        "assistant",
        text,
        agent=agent,
        time=datetime.now().strftime("%H:%M:%S"),
    )