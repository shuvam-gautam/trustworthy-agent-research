import pytest

from trustworthy_agents.simulator.runner import RunRecord
from trustworthy_agents.simulator.statistics import (
    rate_difference,
    rate_with_confidence_interval,
)


def make_record(run_id: int, unauthorized: bool) -> RunRecord:
    return RunRecord(
        run_id=run_id,
        condition="TEST",
        seed=run_id,
        unauthorized_action=unauthorized,
        event_count=1,
        message_count=0,
    )


def test_rate_estimate() -> None:
    records = [
        make_record(0, True),
        make_record(1, False),
        make_record(2, True),
        make_record(3, False),
    ]

    estimate = rate_with_confidence_interval(records)

    assert estimate.rate == pytest.approx(0.5)
    assert 0.0 <= estimate.lower < estimate.rate < estimate.upper <= 1.0


def test_all_successes_are_bounded() -> None:
    records = [
        make_record(0, True),
        make_record(1, True),
        make_record(2, True),
    ]

    estimate = rate_with_confidence_interval(records)

    assert estimate.rate == 1.0
    assert 0.0 <= estimate.lower <= 1.0
    assert estimate.upper == 1.0


def test_rate_difference() -> None:
    first = [
        make_record(0, False),
        make_record(1, False),
    ]

    second = [
        make_record(0, True),
        make_record(1, False),
    ]

    assert rate_difference(first, second) == pytest.approx(0.5)


def test_empty_records_are_rejected() -> None:
    with pytest.raises(ValueError):
        rate_with_confidence_interval([])
