import uuid
from app.schemas import ExecutionSlice, StampedPlan


class Brain:
    def __init__(self) -> None:
        self.current_checkpoint = "A"
        self.history: list[str] = []

    def build_slice(self, start_at: str, end_at: str) -> ExecutionSlice:
        return ExecutionSlice(
            slice_id=str(uuid.uuid4()),
            local_goal=f"move from {start_at} to {end_at}",
            start_at=start_at,
            end_at=end_at,
            stop_at=end_at,
        )

    def mark_pass(self, checkpoint: str) -> None:
        self.current_checkpoint = checkpoint
        self.history.append(checkpoint)

    def next_edges(self, stamped: StampedPlan) -> list[tuple[str, str]]:
        cps = stamped.checkpoints
        return list(zip(cps[:-1], cps[1:]))
