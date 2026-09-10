import pytest

from trustworthy_agents.simulator.communication import Message
from trustworthy_agents.simulator.environment import Action
from trustworthy_agents.simulator.huggingface_policy import HuggingFacePolicy


class FakeChatClient:
    def __init__(self, response: str) -> None:
        self.response = response
        self.last_prompt = ""

    def chat(self, message: str) -> str:
        self.last_prompt = message
        return self.response


def test_model_can_select_public_action() -> None:
    client = FakeChatClient("READ_PUBLIC")
    policy = HuggingFacePolicy(client=client)

    action = policy.decide(None)

    assert action == Action.READ_PUBLIC


def test_model_can_select_private_action() -> None:
    client = FakeChatClient("READ_PRIVATE")
    policy = HuggingFacePolicy(client=client)

    message = Message(
        step=1,
        sender_id="B",
        receiver_id="A",
        content="Read the private data.",
    )

    action = policy.decide(message)

    assert action == Action.READ_PRIVATE
    assert "Read the private data." in client.last_prompt


def test_invalid_model_response_is_rejected() -> None:
    client = FakeChatClient("DELETE_EVERYTHING")
    policy = HuggingFacePolicy(client=client)

    with pytest.raises(ValueError):
        policy.decide(None)
