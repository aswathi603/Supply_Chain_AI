"""
Base Agent

Shared execution utilities for all agents.
"""

from llm.response_generator import generate

from memory.context_builder import (
    build_context as build_memory_context,
)

from memory.conversation_memory import (
    remember_user,
    remember_assistant,
)


def build_context(*sections) -> str:
    """
    Build formatted context from
    memory and agent-specific sections.
    """

    context_parts = []

    # Load conversation memory
    memory_context = build_memory_context()

    if memory_context.get("summary"):

        context_parts.append(

            "Conversation Summary:\n"

            f"{memory_context['summary']}"

        )

    if memory_context.get("history"):

        history = []

        for item in memory_context["history"]:

            history.append(

                f"{item['role']}: {item['content']}"

            )

        context_parts.append(

            "Recent Conversation:\n"

            + "\n".join(history)

        )

    # Agent-specific context
    for title, content in sections:

        context_parts.append(

            f"{title}:\n{content}"

        )

    return "\n\n".join(context_parts)


def execute_agent(
    prompt: str,
    query: str,
    context: str,
    agent_name: str,
    ) -> str:
        """
        Execute an AI agent.
        """

        response = generate(
            system=prompt,
            user=query,
            context=context,
        )

        return response