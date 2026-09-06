# ALFA Multi-Agent Replacement Prototype

> **Python simulation of planned work, guarded execution and replacement on a failed segment**

Alfamultiagentsecured is a small Python prototype that models a multi-step task
flow. The demonstration builds alternative plans, chooses one, executes
segments, checks a Cerber rule, asks Guardian for a verdict and replaces an
executor when the simulated trace fails.

## Structure

```text
app/main.py       executable end-to-end demonstration
app/brain.py      slice and checkpoint handling
app/cerber.py     trace checking
app/guardian.py   verdict generation
app/executor.py   simulated execution
app/storage.py    local state handling
app/llm.py        provider abstraction
```

`app/demo_task.py` supplies the example goal. The code is a simulation and
does not expose a network service or provision independent agents.

## Requirements and setup

The project declares Python 3.11+ and the `pydantic` and `requests`
dependencies in `pyproject.toml`.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -e .
```

For the included demonstration:

```bash
python -m app.main
```

## Configuration

`.env.example` supplies `MODEL_PROVIDER=mock` and `MODEL_NAME=qwen2.5`.
Copy it to a local `.env` only if the selected code path reads it; do not
commit secrets or provider credentials.

## Status and limitations

This is an experimental, deterministic demonstration of control flow. A
`PASS` verdict or a completed demo is not evidence that an external task was
executed safely or that a model response is correct.

## Licence

No licence file is present at repository level.
