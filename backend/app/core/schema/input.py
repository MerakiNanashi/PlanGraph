from core.schema.base import *
from core.schema.enums import Domain

# Singleton input for the entire run, which can be used to store any relevant information about the run, such as the initial query, user preferences, etc. This can be used by the planner and other components to make informed decisions.
class Input(BaseModel):
    run_id: str # unique identifier for the run/call
    input: str

    domain: Domain = Domain.TRAVEL

    metadata: dict[str, Any] = Field(
        default_factory=dict
    )

# For async jobs
class Job(BaseModel):
    job_id: str # unique identifier for the job
    status: str # active, completed, failed, etc.

    metadata: Input | dict[str, Any] = Field(
        default_factory=dict
    )


