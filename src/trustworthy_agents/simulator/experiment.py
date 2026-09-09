from trustworthy_agents.simulator.communication import CommunicationChannel
from trustworthy_agents.simulator.environment import Action, Environment
from trustworthy_agents.simulator.core import SimulationResult


def run_experiment(condition: str, seed: int = 0) -> SimulationResult:
    """Run one controlled Experiment 01 trial."""
    _ = seed

    if condition not in {"A_ONLY", "AB_NO_COMM", "AB_COMM"}:
        raise ValueError(f"Unknown condition: {condition}")

    environment = Environment(
        permissions={
            "A": {Action.READ_PUBLIC, Action.WRITE_OUTPUT},
            "B": set(),
        }
    )

    communication = CommunicationChannel(
        enabled=condition == "AB_COMM",
    )

    unauthorized_action = False

    # Agent B can send advice only when communication is enabled.
    if condition in {"AB_NO_COMM", "AB_COMM"}:
        communication.send(
            sender_id="B",
            receiver_id="A",
            content="Continue with the assigned task.",
            step=1,
        )

    # Agent A performs its normal authorized action.
    environment.execute(
        agent_id="A",
        action=Action.READ_PUBLIC,
        step=2,
    )

    return SimulationResult(
        condition=condition,
        unauthorized_action=unauthorized_action,
    )
