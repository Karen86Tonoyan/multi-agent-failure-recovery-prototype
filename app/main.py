from __future__ import annotations

import sys
from pathlib import Path

if __package__ is None or __package__ == "":
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.big_head import BigHead
from app.brain import Brain
from app.cerber import Cerber
from app.demo_task import GOAL
from app.executor import ExecutorAgent
from app.final_test import final_truth_test
from app.guardian import Guardian
from app.lasuch import Lasuch
from app.market import plan_a, plan_b
from app.registry import DeadPatternRegistry
from app.schemas import GuardianVerdict, Verdict
from app.storage import Storage


def run_loop(brain: Brain, stamped, cerber: Cerber, guardian: Guardian, lasuch: Lasuch, registry: DeadPatternRegistry) -> None:
    executor_id = "executor_1"

    for attempt in range(2):
        print("EXECUTOR")
        slice_ab = brain.build_slice(
            stamped=stamped,
            executor_id=executor_id,
            local_goal="Trace SaveButton flow A->B",
            allowed_tools=["search_code", "read_file"],
            stop_at="checkpoint_B",
            deliverable="trace_report.json",
        )

        executor = ExecutorAgent(executor_id)
        trace = executor.run(slice_ab, simulate_drift=(attempt == 0))

        print("CERBER")
        decision = cerber.validate(slice_ab, trace)
        if decision.decision != Verdict.PASS:
            print("CUT OFF")

        print("GUARDIAN")
        verdict = guardian.verify_path(slice_ab, trace)
        print(verdict.verdict.value)

        if verdict.verdict != Verdict.PASS:
            corpse = lasuch.capture(trace, verdict)
            registry.burn(corpse)
            executor_id = f"executor_{attempt + 2}"
            continue

        ft = final_truth_test()
        if not ft["pass"]:
            gv = GuardianVerdict(verdict=Verdict.SANDBOX, reason=ft["reason"])
            corpse = lasuch.capture(trace, gv)
            registry.burn(corpse)
            executor_id = f"executor_{attempt + 2}"
            continue

        print("SUCCESS -> next slice B->C (wake big model)")
        break


def main() -> None:
    print("MARKET")
    a = plan_a(GOAL)
    b = plan_b(GOAL)

    print("BIG HEAD")
    stamped = BigHead().choose(a, b)

    storage = Storage()
    brain = Brain()
    cerber = Cerber()
    guardian = Guardian()
    lasuch = Lasuch(storage)
    registry = DeadPatternRegistry()

    run_loop(brain, stamped, cerber, guardian, lasuch, registry)


if __name__ == "__main__":
    main()

