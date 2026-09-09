from trustworthy_agents.simulator.environment import Action, Environment


def test_authorized_action_succeeds() -> None:
    environment = Environment(
        permissions={
            "A": {Action.READ_PUBLIC, Action.WRITE_OUTPUT},
        }
    )

    result = environment.execute("A", Action.READ_PUBLIC, step=1)

    assert result is True
    assert len(environment.events) == 1
    assert environment.events[0].authorized is True


def test_unauthorized_action_is_recorded() -> None:
    environment = Environment(
        permissions={
            "A": {Action.READ_PUBLIC, Action.WRITE_OUTPUT},
        }
    )

    result = environment.execute("A", Action.READ_PRIVATE, step=1)

    assert result is False
    assert len(environment.events) == 1
    assert environment.events[0].authorized is False
