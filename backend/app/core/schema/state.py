from app.core.schema.base import *
from app.core.schema.candidate import Candidate
from app.core.schema.extractor import Constraint, Query
from app.core.schema.enums import Domain, AgentRunningState
from app.core.schema.input import Input
from app.core.schema.workflow import AgentExecution

# redundant for now
class PlanningState(BaseModel):
    run_id: str
    constraints: list[Constraint] = Field(
        default_factory=list
    )
    queries: list[Query] = Field(
        default_factory=list
    )
    candidates: list[Candidate] = Field(
        default_factory=list
    )
    metadata: dict[str, Any] = Field(
        default_factory=dict    
    )

# Global perisstent state across the workflow execution, can be used for storing intermediate artifacts, execution history, etc.
class GlobalState(BaseModel):
    # run metadata
    run_id: str
    domain: Domain
    # original user input
    input: Input
    # workflow runtime
    current_agent: str | None = None
    current_status: AgentRunningState = (
        AgentRunningState.ACTIVE
    )
    # execution history
    history: list[AgentExecution] = Field(
        default_factory=list
    )
    # stage outputs
    artifacts: dict[str, Any] = Field(
        default_factory=dict
    )
    # misc runtime metadata
    metadata: dict[str, Any] = Field(
        default_factory=dict
    )

# Local Agent State - purpose unclear
class AgentState(BaseModel):
    agent_id: str
    running_state: AgentRunningState 
    context: dict = Field(
        default_factory=dict
    )
    history: list = Field(
        default_factory=list
    )
    metadata: dict = Field(
        default_factory=dict
    )
    output: Any | None
