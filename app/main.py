import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.market import plan_a, plan_b
from app.big_head import choose
from app.brain import Brain
from app.executor import run
from app.cerber import check
from app.guardian import verify
from app.lasuch import capture
from app.registry import burn
from app.storage import Storage
from app.demo_task import GOAL
from app.final_test import final_truth_test


storage = Storage()
brain = Brain()

print("MARKET")
a = plan_a(GOAL)
b = plan_b(GOAL)

print("BIG HEAD")
plan = choose(a, b)
print(f"winner: {plan.winner}")

edges = brain.next_edges(plan)
executor_counter = 1

for idx, (start_at, end_at) in enumerate(edges):
    print(f"\nSEGMENT {start_at}->{end_at}")

    slice_obj = brain.build_slice(start_at, end_at)

    # symulacja: pierwszy segment ma drift, potem replacement i retry
    simulate_drift = (start_at == "A" and executor_counter == 1)

    trace = run(slice_obj, simulate_drift=simulate_drift)

    print("CERBER")
    ok = check(trace)
    if not ok:
        print("CUT OFF")

    print("GUARDIAN")
    verdict = verify(trace, slice_obj)
    print(verdict.verdict, verdict.reason)

    if verdict.verdict != "PASS":
        segment = f"{start_at}->{end_at}"
        capture(storage, trace, segment)
        burn(segment)
        executor_counter += 1
        print(f"replacement executor_{executor_counter} retries {segment}")

        # retry same segment with new executor, no drift
        trace = run(slice_obj, simulate_drift=False)
        ok = check(trace)
        verdict = verify(trace, slice_obj)
        print(verdict.verdict, verdict.reason)

        if verdict.verdict != "PASS":
            print("hard fail")
            raise SystemExit(1)

    brain.mark_pass(end_at)
    print(f"BRAIN checkpoint -> {brain.current_checkpoint}")

    # wake-on-checkpoint
    print(f"BIG MODEL WAKE at {end_at} -> inject next slice")

print("\nFINAL TRUTH TEST")
ft = final_truth_test()
print(ft)

if not ft["pass"]:
    burn("final_truth_test")
    raise SystemExit(1)

print("\nDONE")
print("history:", brain.history)

