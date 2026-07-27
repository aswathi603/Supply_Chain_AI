"""
Shared simulation utilities.
"""


def simulation_result(

    scenario: str,

    summary: str,

    before=None,

    after=None,

    impact=None,

    recommendation=None,

    confidence=0.80,

):

    return {

        "scenario": scenario,

        "summary": summary,

        "before": before or {},

        "after": after or {},

        "impact": impact or {},

        "recommendation": recommendation,

        "confidence": confidence,

    }