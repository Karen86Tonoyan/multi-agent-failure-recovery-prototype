from __future__ import annotations

from app.schemas import ExecutionTrace, GuardianVerdict
from app.storage import Storage


class Lasuch:
    def __init__(self, storage: Storage) -> None:
        self.storage = storage

    def capture(self, trace: ExecutionTrace, verdict: GuardianVerdict) -> dict:
        corpse = {
            "trace": trace.model_dump(),
            "verdict": verdict.model_dump(),
        }
        self.storage.save(corpse)
        return corpse
