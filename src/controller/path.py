import sys
from pathlib import Path
from typing import Iterable


if getattr(sys, "frozen", False):
    ROOT_PATH = Path(sys.executable).parent
else:
    ROOT_PATH = Path(__file__).parents[2]


def get_available_languages() -> Iterable[str]:
    db_path = ROOT_PATH / "db"
    if not db_path.exists():
        print("Root languagues dir not found")
        return iter([])
    for path in db_path.glob("*"):
        if not path.is_dir():
            continue
        if not (path / "text.db").exists():
            continue
        yield path.name
