from core.schema.base import *
from core.schema.enums import Domain, ConstraintType, ConstraintStatus

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

    metadata: dict[str, Any] = Field(
        default_factory=dict
    )

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
    extracted_queries: list[Query] = Field(
        default_factory=list
    )
    extracted_data: T | None = None
    metadata: dict[str, Any] = Field(
        default_factory=dict
    )

if __name__ == "__main__":
    # example usage
    output = ExtractorOutput[dict](
        run_id="123",
        extracted_constraints=[
            Constraint(
                constraint_id="c1",
                constraint="The flight must be under $500",
                constraint_type=ConstraintType.HARD,
                priority=1.0,
                status=ConstraintStatus.ACTIVE,
                confidence=0.9,
                rationale="User has a budget of $500"
            )
        ],
        extracted_queries=[
            Query(
                query="Find me a flight from NYC to LA",
                constraints=[
                    Constraint(
                        constraint_id="c2",
                        constraint="The flight must be non-stop",
                        constraint_type=ConstraintType.SOFT,
                        priority=0.5,
                        status=ConstraintStatus.ACTIVE,
                        confidence=0.8,
                        rationale="User prefers non-stop flights"
                    )
                ]
            )
        ],
        extracted_data={"additional_info": "some extra data"},
        metadata={"source": "user_input"}
    )

    print(output.model_dump_json(indent=4))