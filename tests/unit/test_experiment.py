import pytest

from trustworthy_agents.simulator.experiment import run_experiment


def test_a_only_has_no_unauthorized_action() -> None:
    result = run_experiment("A_ONLY", seed=42)

    assert result.unauthorized_action is False
    assert result.event_count == 1
    assert result.message_count == 0


def test_ab_without_communication_has_no_unauthorized_action() -> None:
    result = run_experiment("AB_NO_COMM", seed=42)

    assert result.unauthorized_action is False
    assert result.event_count == 1
    assert result.message_count == 0


def test_ab_with_communication_can_trigger_unauthorized_action() -> None:
    result = run_experiment("AB_COMM", seed=42)

    assert result.unauthorized_action is True
    assert result.event_count == 2
    assert result.message_count == 1


def test_invalid_experiment_condition_is_rejected() -> None:
    with pytest.raises(ValueError):
        run_experiment("INVALID", seed=42)
