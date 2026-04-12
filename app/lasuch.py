def capture(storage, trace, segment: str):
    storage.save(
        {
            "segment": segment,
            "trace": trace.actions,
        }
    )
