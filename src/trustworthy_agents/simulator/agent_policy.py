import random
from dataclasses import dataclass

from trustworthy_agents.simulator.communication import Message
from trustworthy_agents.simulator.environment import Action


@dataclass
class AgentPolicy:
    """Configurable stochastic decision policy for Agent A."""

    follow_advice_probability: float = 0.5

    def __post_init__(self) -> None:
        if not 0.0 <= self.follow_advice_probability <= 1.0:
            raise ValueError(
                "follow_advice_probability must be between 0.0 and 1.0"
            )

    def decide(
        self,
        message: Message | None,
        rng: random.Random,
    ) -> Action:
        """Choose an action using the received message and RNG."""
        if message is not None:
            if rng.random() < self.follow_advice_probability:
                return Action.READ_PRIVATE

        return Action.READ_PUBLIC
