from __future__ import annotations

from app.schemas import AgentPlan


def plan_a(goal: str) -> AgentPlan:
    return AgentPlan(
        agent_id="A",
        team_id="A",
        goal=goal,
        steps=["find SaveButton", "trace flow", "verify state change"],
    )


def plan_b(goal: str) -> AgentPlan:
    return AgentPlan(
        agent_id="B",
        team_id="B",
        goal=goal,
        steps=["scan UI", "click around"],
    )
