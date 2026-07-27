"""
Context Builder
"""

from memory.memory_manager import memory


def build_context():

    return {

        "history":

            memory.last(10),

        "summary":

            memory.summary(),

    }