from core.schema.base import *
from core.schema.candidate import Candidate
from core.schema.constraint import Constraint, Query

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