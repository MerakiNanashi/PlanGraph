from app.core.schema.base import *
from app.core.schema.enums import Domain, ConstraintType, ConstraintStatus

T = TypeVar("T")

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


# domain specific 
class Query(BaseModel):
    query: str
    constraints: list[Constraint] = Field(
        default_factory=list
    )

class ExtractorOutput(BaseModel, Generic[T]):
    run_id: str
    extracted_constraints: list[Constraint] = Field(
        default_factory=list
    )
    extracted_data: T | None = None
    metadata: dict[str, Any] = Field(
        default_factory=dict
    )
