from core.utils.base import Path


def save_state(
    state,
    path: str | Path,
) -> None:

    Path(path).write_text(
        state.model_dump_json(
            indent=2
        )
    )


def load_state(
    model_cls,
    path: str | Path,
):

    return model_cls.model_validate_json(
        Path(path).read_text()
    )