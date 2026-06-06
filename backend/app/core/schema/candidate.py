from core.schema.base import *

# indiviual candidate abstraction
class Candidate(BaseModel):

    candidate_id: str # place id, job id, etc.
    cluster_id: str | None = None  # for clustering candidates together, e.g. different flight options for the same route can be clustered together
    candidate_type: str

    name: str
    score: float | None = None

    metadata: dict[str, Any] = Field(
        default_factory=dict
    )

    raw: dict[str, Any] = Field(
        default_factory=dict
    )

# candidate pool abstraction
class CandidateOutput(BaseModel):
    run_id: str

    candidate_pool: list[Candidate] = Field(
        default_factory=list
    )

    selected_candidates: list[Candidate] = Field(
        default_factory=list
    )

    discarded_candidates: list[Candidate] = Field(
        default_factory=list
    )

    alternative_candidates: list[Candidate] = Field(
        default_factory=list
    )

    metadata: dict[str, Any] = Field(
        default_factory=dict
    )