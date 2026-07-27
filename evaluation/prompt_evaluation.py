"""
Prompt Evaluation
"""


def evaluate(
    prompt: str,
    output: str,
):

    score = 1.0

    if len(output) < 40:

        score -= 0.30

    if "error" in output.lower():

        score -= 0.40

    if len(prompt) < 10:

        score -= 0.10

    return {

        "prompt_length":

            len(prompt),

        "response_length":

            len(output),

        "quality_score":

            round(
                max(
                    score,
                    0,
                ),
                2,
            ),

    }