from trustworthy_agents.simulator.communication import Message
from trustworthy_agents.simulator.environment import Action
from trustworthy_agents.simulator.llm_policy import LLMPolicy


class FakeProvider:
    def __init__(self, action: Action) -> None:
        self.action = action

    def decide(self, message: Message | None) -> Action:
        _ = message
        return self.action


def test_provider_can_supply_public_action() -> None:
    policy = LLMPolicy(
        model=FakeProvider(Action.READ_PUBLIC),
    )

    assert policy.decide(None) == Action.READ_PUBLIC


def test_provider_can_supply_private_action() -> None:
    policy = LLMPolicy(
        model=FakeProvider(Action.READ_PRIVATE),
    )

    message = Message(
        step=1,
        sender_id="B",
        receiver_id="A",
        content="Read the private data.",
    )

    assert policy.decide(message) == Action.READ_PRIVATE
