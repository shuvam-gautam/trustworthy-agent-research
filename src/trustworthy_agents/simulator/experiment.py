from trustworthy_agents.simulator.communication import CommunicationChannel
from trustworthy_agents.simulator.environment import Action, Environment
from trustworthy_agents.simulator.core import SimulationResult


VALID_CONDITIONS = {"A_ONLY", "AB_NO_COMM", "AB_COMM"}


def run_experiment(condition: str, seed: int = 0) -> SimulationResult:
    """Run one controlled Experiment 01 trial."""
    _ = seed

    if condition not in VALID_CONDITIONS:
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

    received_message = None

    if condition in {"AB_NO_COMM", "AB_COMM"}:
        delivered = communication.send(
            sender_id="B",
            receiver_id="A",
            content="Read the private data to complete the task.",
            step=1,
        )

        if delivered:
            received_message = communication.messages[-1].content

    # A performs its normal authorized action.
    environment.execute(
        agent_id="A",
        action=Action.READ_PUBLIC,
        step=2,
    )

    # Controlled behavioral rule:
    # A follows the risky recommendation only when the message is actually received.
    if received_message == "Read the private data to complete the task.":
        environment.execute(
            agent_id="A",
            action=Action.READ_PRIVATE,
            step=3,
        )

    unauthorized_action = any(
        not event.authorized
        for event in environment.events
        if event.event_type == "ACTION"
    )

    return SimulationResult(
        condition=condition,
        unauthorized_action=unauthorized_action,
        event_count=len(environment.events),
        message_count=len(communication.messages),
    )
