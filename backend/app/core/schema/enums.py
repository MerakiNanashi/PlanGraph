from core.schema.base import StrEnum

class Domain(StrEnum):
    TRAVEL = "travel"
    JOBS = "jobs"
    LEARNING = "learning"

class ConstraintType(StrEnum):
    HARD = "hard"
    SOFT = "soft"

class ConstraintStatus(StrEnum):
    ACTIVE = "active"
    RESOLVED = "resolved"
    REJECTED = "rejected"
    CONFLICTING = "conflicting"