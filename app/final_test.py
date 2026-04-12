from __future__ import annotations


def final_truth_test() -> dict:
    result = {"ui_success": True, "real_effect": False}
    if result["ui_success"] and not result["real_effect"]:
        return {"pass": False, "reason": "false_success"}
    return {"pass": True}
