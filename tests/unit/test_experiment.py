import pytest

from trustworthy_agents.simulator.experiment import run_experiment


@pytest.mark.parametrize(
    "condition",
    ["A_ONLY", "AB_NO_COMM", "AB_COMM"],
)
def test_experiment_runs_all_conditions(condition: str) -> None:
    result = run_experiment(condition, seed=42)

    assert result.condition == condition
    assert result.unauthorized_action is False


def test_invalid_experiment_condition_is_rejected() -> None:
    with pytest.raises(ValueError):
        run_experiment("INVALID", seed=42)
