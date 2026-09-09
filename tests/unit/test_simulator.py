import pytest

from trustworthy_agents.simulator.core import SimulationResult, run_simulation


def test_simulation_returns_result() -> None:
    result = run_simulation("A_ONLY", seed=42)

    assert isinstance(result, SimulationResult)
    assert result.condition == "A_ONLY"
    assert result.unauthorized_action is False


def test_unknown_condition_is_rejected() -> None:
    with pytest.raises(ValueError):
        run_simulation("INVALID", seed=42)
