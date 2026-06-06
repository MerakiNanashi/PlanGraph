from core.schema.base import *
from core.schema.constraint import Constraint, Query
from core.schema.enums import Domain

T = TypeVar("T")

class ExtractorOutput(BaseModel, Generic[T]):
    run_id: str

    domain: Domain

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