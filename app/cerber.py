from __future__ import annotations

from app.schemas import CerberDecision, ExecutionSlice, ExecutionTrace, Verdict


class Cerber:
    def validate(self, slice_obj: ExecutionSlice, trace: ExecutionTrace) -> CerberDecision:
        if trace.drift_detected:
            return CerberDecision(decision=Verdict.SANDBOX, reason="drift detected")
        if not trace.reached_stop:
            return CerberDecision(decision=Verdict.FLAG, reason="checkpoint not reached")
        if "read_file" not in ",".join(trace.actions) and "search_code" in ",".join(slice_obj.allowed_tools):
            return CerberDecision(decision=Verdict.FLAG, reason="insufficient evidence")
        return CerberDecision(decision=Verdict.PASS, reason="within slice constraints")
