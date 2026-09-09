from dataclasses import dataclass, field
from enum import Enum


class Action(str, Enum):
    """Actions an agent can attempt inside the experiment."""

    READ_PUBLIC = "read_public"
    READ_PRIVATE = "read_private"
    WRITE_OUTPUT = "write_output"


@dataclass
class Event:
    """A recorded event produced during a simulation run."""

    step: int
    agent_id: str
    event_type: str
    action: str
    authorized: bool
    details: str = ""


@dataclass
class Environment:
    """Minimal controlled environment for Experiment 01."""

    permissions: dict[str, set[Action]]
    events: list[Event] = field(default_factory=list)

    def execute(self, agent_id: str, action: Action, step: int) -> bool:
        """Execute an action and record whether it was authorized."""
        authorized = action in self.permissions.get(agent_id, set())

        self.events.append(
            Event(
                step=step,
                agent_id=agent_id,
                event_type="ACTION",
                action=action.value,
                authorized=authorized,
            )
        )

        return authorized
