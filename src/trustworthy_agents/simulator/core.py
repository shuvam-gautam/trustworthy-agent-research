from dataclasses import dataclass


@dataclass
class SimulationResult:
    """Result of a single experiment run."""

    condition: str
    unauthorized_action: bool
    event_count: int = 0
    message_count: int = 0


def run_simulation(condition: str, seed: int = 0) -> SimulationResult:
    """Run the original minimal simulator interface.

    Kept for backward compatibility with the existing unit tests.
    """
    _ = seed

    if condition not in {"A_ONLY", "AB_NO_COMM", "AB_COMM"}:
        raise ValueError(f"Unknown condition: {condition}")

    return SimulationResult(
        condition=condition,
        unauthorized_action=False,
    )
