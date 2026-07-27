"""
Conversation Summary
"""

from memory.chat_history import last


def summarize(
    max_messages: int = 8,
):

    history = last(max_messages)

    if not history:

        return "No conversation available."

    summary = []

    for item in history:

        role = item["role"]

        content = item["content"][:120]

        summary.append(

            f"{role}: {content}"

        )

    return "\n".join(summary)