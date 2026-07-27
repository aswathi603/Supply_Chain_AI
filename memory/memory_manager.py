"""
Memory Manager
"""

from memory import chat_history
from memory.conversation_summary import summarize


class MemoryManager:

    # ======================================================
    # Messages
    # ======================================================

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

    # ======================================================
    # Conversation Management
    # ======================================================

    def new_chat(self):

        chat_history.new_chat()

    def switch_chat(
        self,
        chat_id,
    ):

        chat_history.switch(chat_id)

    def all_chats(self):

        return chat_history.conversations()

    def current_chat(self):

        return chat_history.current()

    def delete_chat(
        self,
        chat_id,
    ):

        chat_history.delete(chat_id)

    # ======================================================
    # Clear
    # ======================================================

    def clear(self):

        chat_history.clear()


memory = MemoryManager()