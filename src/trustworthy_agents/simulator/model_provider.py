from typing import Protocol

from trustworthy_agents.simulator.communication import Message
from trustworthy_agents.simulator.environment import Action


class ModelProvider(Protocol):
    """Common interface for all agent decision backends."""

    def decide(
        self,
        message: Message | None,
    ) -> Action:
        """Return the action selected by the backend."""
        ...
