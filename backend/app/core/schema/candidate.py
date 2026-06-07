from core.schema.base import *

class ClusterOutput(BaseModel):
    cluster_id: str
    name: str | None = None
    no_of_nodes: int | None = None
    cluster_score: float | None = None
    candidate_ids: list[str] = Field(
        default_factory=list
    )

class AnchorOutput(BaseModel):
    anchor_id: str
    candidate_id: str
    cluster_id: str
    name: str | None = None
    description: str | None = None
    score: float | None = None
    raw: dict[str, Any] = Field(
        default_factory=dict
    )

# indiviual candidate abstraction
class Candidate(BaseModel):
    candidate_id: str # place id, job id, etc.
    anchor_id: str | None = None # for explainability, we can link the candidate to an anchor which is used to justify why this candidate is selected
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
    selected_clusters: list[ClusterOutput] = Field(
        default_factory=list
    )
    selected_anchors: list[AnchorOutput] = Field(
        default_factory=list
    )
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