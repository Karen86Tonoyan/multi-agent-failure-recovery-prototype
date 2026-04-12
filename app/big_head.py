from app.schemas import StampedPlan


def choose(a, b):
    winner = a if len(a.steps) > len(b.steps) else b
    return StampedPlan(
        plan_id="1",
        winner=winner.agent_id,
        steps=winner.steps,
        checkpoints=["A", "B", "C", "D"],
    )
