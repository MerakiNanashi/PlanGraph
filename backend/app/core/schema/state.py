from core.schema.base import *
from core.schema.candidate import CandidateOutput, Cluster, Anchor, Candidate
from core.schema.extractor import Constraint, Query
from core.schema.enums import Domain, AgentRunningState
from core.schema.input import Input, Job
from core.schema.workflow import AgentExecution

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

# Local Agent State
class AgentState(BaseModel):
    agent_id: str
    running_state: AgentRunningState 
    context: dict = Field(
        default_factory=dict
    )
    history: list = Field(
        default_factory=list
    )
    output: Any | None

if __name__ == "__main__":
    # example usage
    state = GlobalState(
        run_id="123",
        domain=Domain.TRAVEL,
        input=Input(
            run_id="123",
            input="Find me a flight from NYC to LA next week",
            domain=Domain.TRAVEL,
            metadata={
                "user_id": "user_123",
                "timestamp": "2024-01-01T12:00:00Z"
            }
        )
    )
    print(state.model_dump_json(indent=4))