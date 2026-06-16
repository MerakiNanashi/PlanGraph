from app.core.utils.base import Path, json

def dump_json(
    data,
    path: str | Path,
) -> None:
    with open(
        path,
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(
            data,
            f,
            indent=2,
            ensure_ascii=False,
        )


def load_json(
    path: str | Path,
):
    with open(
        path,
        "r",
        encoding="utf-8",
    ) as f:
        return json.load(f)
    
def normalize_json():
    pass