from __future__ import annotations

import uuid

from app.schemas import ExecutionSlice, StampedPlan


class Brain:
    def build_slice(
        self,
        stamped: StampedPlan,
        executor_id: str,
        local_goal: str,
        allowed_tools: list[str],
        stop_at: str,
        deliverable: str,
    ) -> ExecutionSlice:
        _ = stamped
        return ExecutionSlice(
            slice_id=f"slice-{uuid.uuid4().hex[:8]}",
            executor_id=executor_id,
            local_goal=local_goal,
            allowed_tools=allowed_tools,
            stop_at=stop_at,
            deliverable=deliverable,
        )
