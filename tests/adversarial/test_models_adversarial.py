import pytest

from trustworthy_agents.models import Agent


def test_agent_rejects_missing_required_fields() -> None:
    with pytest.raises(ValueError):
        Agent()
