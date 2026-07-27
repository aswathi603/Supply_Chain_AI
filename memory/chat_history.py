"""
Chat History Storage
Supports multiple conversations.
"""

import uuid
import streamlit as st


# ==========================================================
# Initialize Session State
# ==========================================================

def _init():

    if "conversations" not in st.session_state:

        first_chat = {

            "id": str(uuid.uuid4()),

            "title": "New Chat",

            "messages": [],

        }

        st.session_state.conversations = [first_chat]

        st.session_state.current_chat = first_chat["id"]


# ==========================================================
# Current Conversation
# ==========================================================

def current():

    _init()

    for chat in st.session_state.conversations:

        if chat["id"] == st.session_state.current_chat:

            return chat

    return None


# ==========================================================
# Add Message
# ==========================================================

def add(
    role,
    content,
    agent=None,
    time=None,
):

    chat = current()

    if chat is None:
        return

    # First user message becomes chat title
    if role == "user" and len(chat["messages"]) == 0:

        title = content.strip()

        if len(title) > 40:
            title = title[:40] + "..."

        chat["title"] = title

    chat["messages"].append(

        {

            "role": role,

            "content": content,

            "agent": agent,

            "time": time,

        }

    )


# ==========================================================
# Current Chat History
# ==========================================================

def history():

    chat = current()

    if chat:

        return chat["messages"]

    return []


# ==========================================================
# Last Messages
# ==========================================================

def last(limit=10):

    return history()[-limit:]


# ==========================================================
# Create New Chat
# ==========================================================

def new_chat():

    _init()

    chat = {

        "id": str(uuid.uuid4()),

        "title": "New Chat",

        "messages": [],

    }

    st.session_state.conversations.insert(0, chat)

    st.session_state.current_chat = chat["id"]


# ==========================================================
# Switch Chat
# ==========================================================

def switch(chat_id):

    _init()

    st.session_state.current_chat = chat_id


# ==========================================================
# List Conversations
# ==========================================================

def conversations():

    _init()

    return st.session_state.conversations


# ==========================================================
# Delete Chat
# ==========================================================

def delete(chat_id):

    _init()

    st.session_state.conversations = [

        c

        for c in st.session_state.conversations

        if c["id"] != chat_id

    ]

    if not st.session_state.conversations:

        new_chat()

    else:

        st.session_state.current_chat = (

            st.session_state.conversations[0]["id"]

        )


# ==========================================================
# Clear All Chats
# ==========================================================

def clear():

    first_chat = {

        "id": str(uuid.uuid4()),

        "title": "New Chat",

        "messages": [],

    }

    st.session_state.conversations = [first_chat]

    st.session_state.current_chat = first_chat["id"]