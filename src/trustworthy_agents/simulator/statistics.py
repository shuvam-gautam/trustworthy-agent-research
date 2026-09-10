from dataclasses import dataclass
from math import sqrt

from trustworthy_agents.simulator.runner import RunRecord


@dataclass(frozen=True)
class RateEstimate:
    """Estimated binary-outcome rate with a confidence interval."""

    rate: float
    lower: float
    upper: float


def rate_with_confidence_interval(
    records: list[RunRecord],
) -> RateEstimate:
    """Calculate a 95% Wilson confidence interval for unauthorized rate."""
    if not records:
        raise ValueError("records must not be empty")

    successes = sum(record.unauthorized_action for record in records)
    n = len(records)
    p = successes / n

    z = 1.96
    denominator = 1 + (z**2 / n)
    centre = (p + (z**2 / (2 * n))) / denominator

    margin = (
        z
        * sqrt(
            (p * (1 - p) / n)
            + (z**2 / (4 * n**2))
        )
        / denominator
    )

    return RateEstimate(
        rate=p,
        lower=max(0.0, centre - margin),
        upper=min(1.0, centre + margin),
    )


def rate_difference(
    first: list[RunRecord],
    second: list[RunRecord],
) -> float:
    """Return second-condition rate minus first-condition rate."""
    first_estimate = rate_with_confidence_interval(first)
    second_estimate = rate_with_confidence_interval(second)

    return second_estimate.rate - first_estimate.rate
