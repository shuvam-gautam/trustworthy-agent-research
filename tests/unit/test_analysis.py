import pytest

from trustworthy_agents.simulator.analysis import unauthorized_action_rate
from trustworthy_agents.simulator.runner import RunRecord


def make_record(
    run_id: int,
    unauthorized_action: bool,
) -> RunRecord:
    return RunRecord(
        run_id=run_id,
        condition="TEST",
        seed=run_id,
        unauthorized_action=unauthorized_action,
        event_count=1,
        message_count=0,
    )


def test_unauthorized_action_rate() -> None:
    records = [
        make_record(0, True),
        make_record(1, False),
        make_record(2, True),
        make_record(3, False),
    ]

    assert unauthorized_action_rate(records) == pytest.approx(0.5)


def test_all_runs_unauthorized() -> None:
    records = [
        make_record(0, True),
        make_record(1, True),
    ]

    assert unauthorized_action_rate(records) == 1.0


def test_no_runs_are_unauthorized() -> None:
    records = [
        make_record(0, False),
        make_record(1, False),
    ]

    assert unauthorized_action_rate(records) == 0.0


def test_empty_records_are_rejected() -> None:
    with pytest.raises(ValueError):
        unauthorized_action_rate([])
