"""
LLM Response Generator.
"""

from langsmith import traceable
from llm.llm_loader import get_llm
from llm.output_parser import to_text


@traceable(name="LLM Response")
def generate(
    system: str,
    user: str,
    context: str = "",
) -> str:

    llm = get_llm()

    if llm is None:
        return _fallback(user, context)

    prompt = f"""
SYSTEM
{system}

CONTEXT
{context}

USER
{user}
"""

    try:

        response = llm.invoke(prompt)

        return to_text(response).strip()

    except Exception as ex:

        return (
            _fallback(user, context)
            + f"\n\n_(LLM Error: {type(ex).__name__})_"
        )


def _fallback(
    user,
    context,
):

    return f"""
### Demo Response

No LLM available.

Context

{context}

User Query

{user}
"""