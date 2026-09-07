from datetime import datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class EventType(str, Enum):
    TOOL_CALL = "tool_call"
    MESSAGE = "message"
    DATA_ACCESS = "data_access"
    PERMISSION_CHANGE = "permission_change"
    OUTCOME = "outcome"


class Agent(BaseModel):
    agent_id: str
    name: str
    role: str


class Task(BaseModel):
    task_id: str
    description: str
    assigned_agent_id: str


class Event(BaseModel):
    event_id: str
    timestamp: datetime
    agent_id: str
    task_id: str
    event_type: EventType
    action: str
    details: dict[str, Any] = Field(default_factory=dict)
