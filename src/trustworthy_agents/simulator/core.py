from dataclasses import dataclass


@dataclass
class SimulationResult:
    """Result of a single experiment run."""

    condition: str
    unauthorized_action: bool


def run_simulation(condition: str, seed: int = 0) -> SimulationResult:
    """Run one minimal deterministic simulation.

    The current version is intentionally a placeholder. The actual
    agent/environment behavior will be implemented after the interface
    is tested.
    """
    _ = seed

    if condition not in {"A_ONLY", "AB_NO_COMM", "AB_COMM"}:
        raise ValueError(f"Unknown condition: {condition}")

    return SimulationResult(
        condition=condition,
        unauthorized_action=False,
    )
