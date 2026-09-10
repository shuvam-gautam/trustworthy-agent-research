from dataclasses import dataclass
from typing import Protocol

from trustworthy_agents.simulator.communication import Message
from trustworthy_agents.simulator.environment import Action


class DecisionModel(Protocol):
    """Interface for a model that selects an agent action."""

    def decide(
        self,
        message: Message | None,
    ) -> Action:
        """Return the action selected by the model."""
        ...


@dataclass
class LLMPolicy:
    """Agent policy backed by an external decision model."""

    model: DecisionModel

    def decide(self, message: Message | None) -> Action:
        """Delegate the decision to the configured model."""
        return self.model.decide(message)
