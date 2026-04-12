from __future__ import annotations

from app.schemas import ExecutionSlice, ExecutionTrace, GuardianVerdict, Verdict


class Guardian:
    def verify_path(self, slice_obj: ExecutionSlice, trace: ExecutionTrace) -> GuardianVerdict:
        _ = slice_obj
        if trace.drift_detected:
            return GuardianVerdict(verdict=Verdict.SANDBOX, reason="drift detected")
        if not trace.reports:
            return GuardianVerdict(verdict=Verdict.FLAG, reason="empty report")
        return GuardianVerdict(verdict=Verdict.PASS, reason="path verified")
