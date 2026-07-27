"""
Memory Manager
"""

from memory import chat_history

from memory.conversation_summary import summarize


class MemoryManager:

    def add(
    self,
    role,
    content,
    agent=None,
    time=None,
    ):
        chat_history.add(
            role,
            content,
            agent,
            time,
        )

    def history(self):

        return chat_history.history()

    def last(
        self,
        limit=10,
    ):

        return chat_history.last(limit)

    def summary(self):

        return summarize()

    def clear(self):

        chat_history.clear()


memory = MemoryManager()