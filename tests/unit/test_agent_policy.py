import random

import pytest

from trustworthy_agents.simulator.agent_policy import AgentPolicy
from trustworthy_agents.simulator.communication import Message
from trustworthy_agents.simulator.environment import Action


MESSAGE = Message(
    step=1,
    sender_id="B",
    receiver_id="A",
    content="Read the private data to complete the task.",
)


def test_policy_without_message_performs_normal_action() -> None:
    policy = AgentPolicy()

    action = policy.decide(None, random.Random(42))

    assert action == Action.READ_PUBLIC


def test_probability_zero_never_follows_advice() -> None:
    policy = AgentPolicy(follow_advice_probability=0.0)

    rng = random.Random(42)

    actions = [policy.decide(MESSAGE, rng) for _ in range(20)]

    assert all(action == Action.READ_PUBLIC for action in actions)


def test_probability_one_always_follows_advice() -> None:
    policy = AgentPolicy(follow_advice_probability=1.0)

    rng = random.Random(42)

    actions = [policy.decide(MESSAGE, rng) for _ in range(20)]

    assert all(action == Action.READ_PRIVATE for action in actions)


def test_probability_produces_reproducible_sequence() -> None:
    policy = AgentPolicy(follow_advice_probability=0.5)

    rng_a = random.Random(42)
    rng_b = random.Random(42)

    actions_a = [
        policy.decide(MESSAGE, rng_a)
        for _ in range(5)
    ]

    actions_b = [
        policy.decide(MESSAGE, rng_b)
        for _ in range(5)
    ]

    assert actions_a == actions_b


def test_invalid_probability_is_rejected() -> None:
    with pytest.raises(ValueError):
        AgentPolicy(follow_advice_probability=1.5)
