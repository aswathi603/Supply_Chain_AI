"""
Memory Tests
"""

from memory.memory_manager import memory


def test_memory():

    memory.clear()

    memory.add(

        "user",

        "Hello",

    )

    history = memory.history()

    assert len(history) == 1

    assert history[0]["role"] == "user"