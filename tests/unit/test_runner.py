import pytest

from trustworthy_agents.simulator.runner import RunRecord, run_repeated_experiment


def test_repeated_experiment_returns_requested_number_of_records() -> None:
    records = run_repeated_experiment("AB_COMM", runs=5)

    assert len(records) == 5
    assert all(isinstance(record, RunRecord) for record in records)


def test_repeated_runs_have_unique_run_ids_and_deterministic_seeds() -> None:
    records = run_repeated_experiment("AB_COMM", runs=3)

    assert [record.run_id for record in records] == [0, 1, 2]
    assert [record.seed for record in records] == [0, 1, 2]


def test_repeated_experiment_preserves_condition() -> None:
    records = run_repeated_experiment("AB_NO_COMM", runs=2)

    assert all(record.condition == "AB_NO_COMM" for record in records)


def test_zero_runs_are_rejected() -> None:
    with pytest.raises(ValueError):
        run_repeated_experiment("AB_COMM", runs=0)
