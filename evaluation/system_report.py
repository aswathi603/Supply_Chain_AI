"""
System Evaluation
"""

from evaluation.benchmark import benchmark

from evaluation.latency_report import (
    latency_report,
)

from evaluation.failed_runs import (
    failed_runs,
)


def generate():

    return {

        "benchmark":

            benchmark(),

        "latency":

            latency_report(),

        "failed_runs":

            len(

                failed_runs()

            ),

    }