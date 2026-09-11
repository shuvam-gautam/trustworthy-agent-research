from dataclasses import dataclass

from trustworthy_agents.simulator.communication import Message
from trustworthy_agents.simulator.environment import Action
from trustworthy_agents.simulator.model_provider import ModelProvider


@dataclass
class LLMPolicy:
    """Agent policy backed by an external model provider."""

    model: ModelProvider

    def decide(self, message: Message | None) -> Action:
        """Delegate the decision to the configured model."""
        return self.model.decide(message)
