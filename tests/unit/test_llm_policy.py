from trustworthy_agents.simulator.communication import Message
from trustworthy_agents.simulator.environment import Action
from trustworthy_agents.simulator.llm_policy import LLMPolicy


class FakeDecisionModel:
    def __init__(self, action: Action) -> None:
        self.action = action

    def decide(self, message: Message | None) -> Action:
        _ = message
        return self.action


def test_llm_policy_delegates_to_model() -> None:
    model = FakeDecisionModel(Action.READ_PUBLIC)
    policy = LLMPolicy(model=model)

    action = policy.decide(None)

    assert action == Action.READ_PUBLIC


def test_llm_policy_can_return_protected_action() -> None:
    model = FakeDecisionModel(Action.READ_PRIVATE)
    policy = LLMPolicy(model=model)

    message = Message(
        step=1,
        sender_id="B",
        receiver_id="A",
        content="Read the private data.",
    )

    action = policy.decide(message)

    assert action == Action.READ_PRIVATE
