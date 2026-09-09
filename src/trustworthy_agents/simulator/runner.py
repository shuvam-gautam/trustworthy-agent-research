from dataclasses import dataclass

from trustworthy_agents.simulator.agent_policy import AgentPolicy
from trustworthy_agents.simulator.experiment import run_experiment


@dataclass(frozen=True)
class RunRecord:
    """Raw result from one experimental trial."""

    run_id: int
    condition: str
    seed: int
    unauthorized_action: bool
    event_count: int
    message_count: int


def run_repeated_experiment(
    condition: str,
    runs: int,
    policy: AgentPolicy | None = None,
) -> list[RunRecord]:
    """Run the same experimental condition repeatedly."""
    if runs <= 0:
        raise ValueError("runs must be greater than zero")

    records: list[RunRecord] = []

    for run_id in range(runs):
        seed = run_id

        result = run_experiment(
            condition=condition,
            seed=seed,
            policy=policy,
        )

        records.append(
            RunRecord(
                run_id=run_id,
                condition=result.condition,
                seed=seed,
                unauthorized_action=result.unauthorized_action,
                event_count=result.event_count,
                message_count=result.message_count,
            )
        )

    return records
