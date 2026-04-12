from __future__ import annotations

from pathlib import Path

BASE = Path(".")


def read_file(path: str) -> str:
    p = BASE / path
    return p.read_text(encoding="utf-8") if p.exists() else ""


def search_code(query: str) -> list[str]:
    hits: list[str] = []
    for p in BASE.rglob("*.py"):
        try:
            txt = p.read_text(encoding="utf-8")
            if query.lower() in txt.lower():
                hits.append(str(p))
        except Exception:
            pass
    return hits[:10]


def apply_patch(path: str, content: str) -> str:
    p = BASE / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    return "patched"


def run_tests() -> dict:
    return {"passed": True, "details": "mock"}
