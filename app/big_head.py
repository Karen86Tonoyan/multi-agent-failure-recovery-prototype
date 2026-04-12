from __future__ import annotations

import uuid

from app.llm import choose_plan_with_llm
from app.schemas import AgentPlan, StampedPlan


class BigHead:
    def choose(self, a: AgentPlan, b: AgentPlan) -> StampedPlan:
        decision = choose_plan_with_llm(a.model_dump(), b.model_dump())
        winner = a if decision.get("winner") in ("A", a.agent_id) else b

        return StampedPlan(
            plan_id=f"plan-{uuid.uuid4().hex[:8]}",
            winner_agent_id=winner.agent_id,
            winner_team_id=winner.team_id,
            goal=winner.goal,
            approved_steps=winner.steps,
            conditions=[
                "report every step",
                "stop at checkpoint_B",
                "no continuation beyond slice",
            ],
            version=1,
        )
