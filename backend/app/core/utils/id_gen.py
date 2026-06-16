from app.core.utils.base import uuid4

# General ID gen with prefix
def _generate(prefix: str) -> str:
    return f"{prefix}_{uuid4().hex}"

def user_id() -> str:
    return _generate("usr")

def run_id() -> str:
    return _generate("run")

def job_id() -> str:
    return _generate("job")

def artifact_id() -> str:
    return _generate("art")

