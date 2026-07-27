"""
Tracing utilities
"""

from functools import wraps

from config.langsmith_config import (
    LANGSMITH_ENABLED,
)

from graph.logger import (
    log_event,
)


def trace(name: str):

    def decorator(fn):

        @wraps(fn)

        def wrapper(*args, **kwargs):

            if LANGSMITH_ENABLED:

                log_event(
                    "TRACE",
                    f"Running {name}",
                )

            return fn(
                *args,
                **kwargs,
            )

        return wrapper

    return decorator