from core.schema.base import *
from core.schema.enums import AgentRunningState

T = TypeVar("T")

class AgentExecution(BaseModel):
    order: int
    agent_name: str
    running_state: AgentRunningState = AgentRunningState.ACTIVE
    started_at: datetime | None = None
    completed_at: datetime | None = None

class BaseWorkflow:
    stages: list[type[T]]