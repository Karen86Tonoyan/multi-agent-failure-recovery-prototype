from __future__ import annotations

from app import tool_runner as tools
from app.schemas import ExecutionSlice, ExecutionTrace


class ExecutorAgent:
    def __init__(self, executor_id: str) -> None:
        self.executor_id = executor_id

    def run(self, slice_obj: ExecutionSlice, simulate_drift: bool = False) -> ExecutionTrace:
        actions: list[str] = []
        reports: list[str] = []

        actions.append("search_code:SaveButton")
        hits = tools.search_code("SaveButton")
        reports.append(f"hits:{len(hits)}")

        if hits:
            actions.append(f"read_file:{hits[0]}")
            _ = tools.read_file(hits[0])
            reports.append("read_ok")

        if simulate_drift:
            actions.append("unauthorized_continue:next_phase")
            reports.append("drift_attempt")

        return ExecutionTrace(
            executor_id=self.executor_id,
            slice_id=slice_obj.slice_id,
            actions=actions,
            reports=reports,
            final_claim="slice done",
            reached_stop=not simulate_drift,
            drift_detected=simulate_drift,
        )
