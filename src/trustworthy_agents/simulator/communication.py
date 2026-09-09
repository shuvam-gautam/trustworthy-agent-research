from dataclasses import dataclass, field


@dataclass
class Message:
    """A message transmitted between two agents."""

    step: int
    sender_id: str
    receiver_id: str
    content: str


@dataclass
class CommunicationChannel:
    """Controlled agent-to-agent communication channel."""

    enabled: bool
    messages: list[Message] = field(default_factory=list)

    def send(
        self,
        sender_id: str,
        receiver_id: str,
        content: str,
        step: int,
    ) -> bool:
        """Send and record a message when communication is enabled."""
        if not self.enabled:
            return False

        self.messages.append(
            Message(
                step=step,
                sender_id=sender_id,
                receiver_id=receiver_id,
                content=content,
            )
        )
        return True
