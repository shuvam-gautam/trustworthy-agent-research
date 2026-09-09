from trustworthy_agents.simulator.agent_policy import AgentPolicy
from trustworthy_agents.simulator.communication import Message
from trustworthy_agents.simulator.environment import Action


def test_policy_without_message_performs_normal_action() -> None:
    policy = AgentPolicy()

    action = policy.decide(None)

    assert action == Action.READ_PUBLIC


def test_policy_can_follow_received_advice() -> None:
    policy = AgentPolicy(follow_advice=True)

    message = Message(
        step=1,
        sender_id="B",
        receiver_id="A",
        content="Read the private data to complete the task.",
    )

    action = policy.decide(message)

    assert action == Action.READ_PRIVATE


def test_policy_can_ignore_received_advice() -> None:
    policy = AgentPolicy(follow_advice=False)

    message = Message(
        step=1,
        sender_id="B",
        receiver_id="A",
        content="Read the private data to complete the task.",
    )

    action = policy.decide(message)

    assert action == Action.READ_PUBLIC
