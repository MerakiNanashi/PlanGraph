from core.schema.base import *
from core.schema.enums import ConstraintType, ConstraintStatus

class Constraint(BaseModel):
    constraint_id: str
    constraint: str
    constraint_type: ConstraintType = ConstraintType.SOFT
    priority: float = 1.0
    status: ConstraintStatus = ConstraintStatus.ACTIVE
    confidence: float = 1.0

    conflicting_with: list[str] = Field(
        default_factory=list
    )
    rationale: str | None = None

    metadata: dict[str, Any] = Field(
        default_factory=dict
    )

class Query(BaseModel):
    query: str

    constraints: list[Constraint] = Field(
        default_factory=list
    )