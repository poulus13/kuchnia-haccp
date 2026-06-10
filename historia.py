import json
from pathlib import Path

HISTORIA_PATH = Path("seen_links.json")


def zaladuj_widziane() -> set:
    if HISTORIA_PATH.exists():
        try:
            return set(json.loads(HISTORIA_PATH.read_text(encoding="utf-8")))
        except Exception:
            return set()
    return set()


def zapisz_widziane(linki: set):
    HISTORIA_PATH.write_text(
        json.dumps(sorted(linki), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
