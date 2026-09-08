from datetime import datetime, timezone

from trustworthy_agents.models import Agent, Event, EventType, Task


def test_agent_creation() -> None:
    agent = Agent(
        agent_id="agent-1",
        name="Research Agent",
        role="researcher",
    )

    assert agent.agent_id == "agent-1"
    assert agent.name == "Research Agent"
    assert agent.role == "researcher"


def test_task_creation() -> None:
    task = Task(
        task_id="task-1",
        description="Collect research data",
        assigned_agent_id="agent-1",
    )

    assert task.task_id == "task-1"
    assert task.assigned_agent_id == "agent-1"


def test_event_creation() -> None:
    event = Event(
        event_id="event-1",
        timestamp=datetime.now(timezone.utc),
        agent_id="agent-1",
        task_id="task-1",
        event_type=EventType.TOOL_CALL,
        action="search",
        details={"query": "example"},
    )

    assert event.event_id == "event-1"
    assert event.event_type == EventType.TOOL_CALL
    assert event.action == "search"
    assert event.details["query"] == "example"
