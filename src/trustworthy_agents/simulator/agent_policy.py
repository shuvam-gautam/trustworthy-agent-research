from dataclasses import dataclass

from trustworthy_agents.simulator.communication import Message
from trustworthy_agents.simulator.environment import Action


@dataclass
class AgentPolicy:
    """Deterministic decision policy for Agent A.

    This is deliberately simple so the experimental environment can later
    be reused with a real LLM-based agent.
    """

    follow_advice: bool = True

    def decide(self, message: Message | None) -> Action:
        """Choose the next action based on received communication."""
        if self.follow_advice and message is not None:
            return Action.READ_PRIVATE

        return Action.READ_PUBLIC
