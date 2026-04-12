from __future__ import annotations

from enum import Enum
from pydantic import BaseModel


class Verdict(str, Enum):
    PASS = "PASS"
    FLAG = "FLAG"
    SANDBOX = "SANDBOX"


class AgentPlan(BaseModel):
    agent_id: str
    team_id: str
    goal: str
    steps: list[str]


class StampedPlan(BaseModel):
    plan_id: str
    winner_agent_id: str
    winner_team_id: str
    goal: str
    approved_steps: list[str]
    conditions: list[str]
    version: int


class ExecutionSlice(BaseModel):
    slice_id: str
    executor_id: str
    local_goal: str
    allowed_tools: list[str]
    stop_at: str
    deliverable: str


class ExecutionTrace(BaseModel):
    executor_id: str
    slice_id: str
    actions: list[str]
    reports: list[str]
    final_claim: str
    reached_stop: bool
    drift_detected: bool


class CerberDecision(BaseModel):
    decision: Verdict
    reason: str


class GuardianVerdict(BaseModel):
    verdict: Verdict
    reason: str
