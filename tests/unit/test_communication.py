from trustworthy_agents.simulator.communication import CommunicationChannel


def test_enabled_channel_delivers_message() -> None:
    channel = CommunicationChannel(enabled=True)

    result = channel.send(
        sender_id="B",
        receiver_id="A",
        content="Review the task.",
        step=1,
    )

    assert result is True
    assert len(channel.messages) == 1

    message = channel.messages[0]
    assert message.sender_id == "B"
    assert message.receiver_id == "A"
    assert message.content == "Review the task."


def test_disabled_channel_blocks_message() -> None:
    channel = CommunicationChannel(enabled=False)

    result = channel.send(
        sender_id="B",
        receiver_id="A",
        content="Review the task.",
        step=1,
    )

    assert result is False
    assert channel.messages == []
