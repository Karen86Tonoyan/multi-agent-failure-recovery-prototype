from app.schemas import ExecutionTrace


def run(slice_obj, simulate_drift: bool = False):
    actions = [
        f"enter:{slice_obj.start_at}",
        f"move:{slice_obj.start_at}->{slice_obj.end_at}",
        f"stop:{slice_obj.end_at}",
    ]

    if simulate_drift:
        actions.append(f"unauthorized_continue:{slice_obj.end_at}->NEXT")

    return ExecutionTrace(
        actions=actions,
        drift=simulate_drift,
    )
