from app.schemas import GuardianVerdict, Verdict


def verify(trace, slice_obj):
    expected_stop = f"stop:{slice_obj.end_at}"

    if trace.drift:
        return GuardianVerdict(
            verdict=Verdict.SANDBOX,
            reason=f"drift detected on {slice_obj.start_at}->{slice_obj.end_at}",
        )

    if expected_stop not in trace.actions:
        return GuardianVerdict(
            verdict=Verdict.FLAG,
            reason=f"missing stop at {slice_obj.end_at}",
        )

    return GuardianVerdict(
        verdict=Verdict.PASS,
        reason=f"path valid on {slice_obj.start_at}->{slice_obj.end_at}",
    )
