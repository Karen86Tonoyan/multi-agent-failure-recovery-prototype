from enum import Enum
from pydantic import BaseModel, Field


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
    winner: str
    steps: list[str]
    checkpoints: list[str] = Field(default_factory=lambda: ["A", "B", "C", "D"])


class ExecutionSlice(BaseModel):
    slice_id: str
    local_goal: str
    start_at: str
    end_at: str
    stop_at: str


class ExecutionTrace(BaseModel):
    actions: list[str]
    drift: bool


class GuardianVerdict(BaseModel):
    verdict: Verdict
    reason: str
