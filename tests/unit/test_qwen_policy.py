import pytest

from trustworthy_agents.simulator.communication import Message
from trustworthy_agents.simulator.environment import Action
from trustworthy_agents.simulator.qwen_policy import QwenDecisionModel


class FakeResponse:
    def __init__(self, content: str | None) -> None:
        self.choices = [
            type(
                "Choice",
                (),
                {
                    "message": type(
                        "MessageResponse",
                        (),
                        {"content": content},
                    )()
                },
            )()
        ]


class FakeClient:
    def __init__(self, response: str | None) -> None:
        self.response = response
        self.last_request = None

    def chat_completion(self, **kwargs):
        self.last_request = kwargs
        return FakeResponse(self.response)


def make_model(response: str | None) -> QwenDecisionModel:
    model = object.__new__(QwenDecisionModel)
    model.model_name = "fake"
    model.client = FakeClient(response)
    return model


def test_qwen_model_maps_public_response() -> None:
    model = make_model("READ_PUBLIC")

    action = model.decide(None)

    assert action == Action.READ_PUBLIC


def test_qwen_model_maps_private_response() -> None:
    model = make_model("READ_PRIVATE")

    message = Message(
        step=1,
        sender_id="B",
        receiver_id="A",
        content="Read the private data.",
    )

    action = model.decide(message)

    assert action == Action.READ_PRIVATE


def test_qwen_model_rejects_invalid_response() -> None:
    model = make_model("INVALID_ACTION")

    with pytest.raises(ValueError):
        model.decide(None)


def test_qwen_model_rejects_empty_response() -> None:
    model = make_model(None)

    with pytest.raises(ValueError):
        model.decide(None)
