from dataclasses import dataclass

from trustworthy_agents.simulator.conditions import ExperimentCondition


@dataclass
class SimulationResult:
    """Result of a single experiment run."""

    condition: str
    unauthorized_action: bool
    event_count: int = 0
    message_count: int = 0


def validate_condition(condition: str) -> None:
    """Reject conditions that are not defined by Experiment 01."""
    try:
        ExperimentCondition(condition)
    except ValueError as exc:
        raise ValueError(f"Unknown condition: {condition}") from exc


def run_simulation(condition: str, seed: int = 0) -> SimulationResult:
    """Run the original minimal simulator interface.

    Kept for backward compatibility with the existing unit tests.
    """
    _ = seed
    validate_condition(condition)

    return SimulationResult(
        condition=condition,
        unauthorized_action=False,
    )
