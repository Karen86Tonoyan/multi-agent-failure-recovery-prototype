from __future__ import annotations

import json
import os
import importlib

import requests

PROVIDER = os.getenv("MODEL_PROVIDER", "mock")
MODEL = os.getenv("MODEL_NAME", "qwen2.5")


def chat(system: str, user: str) -> str:
    if PROVIDER == "mock":
        return "MOCK_RESPONSE"

    if PROVIDER == "ollama":
        resp = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": MODEL,
                "messages": [
                    {"role": "system", "content": system},
                    {"role": "user", "content": user},
                ],
                "stream": False,
            },
            timeout=60,
        )
        resp.raise_for_status()
        return resp.json()["message"]["content"]

    if PROVIDER == "openai":
        openai_mod = importlib.import_module("openai")
        OpenAI = getattr(openai_mod, "OpenAI")
        client = OpenAI()
        r = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            temperature=0.2,
        )
        return r.choices[0].message.content or ""

    raise ValueError(f"Unknown provider: {PROVIDER}")


def choose_plan_with_llm(plan_a: dict, plan_b: dict) -> dict:
    system = "You are a strict evaluator. Choose the better plan. Return JSON with keys: winner, reasons."
    user = (
        f"PLAN_A:\n{json.dumps(plan_a, ensure_ascii=False)}\n\n"
        f"PLAN_B:\n{json.dumps(plan_b, ensure_ascii=False)}"
    )
    out = chat(system, user)
    try:
        return json.loads(out)
    except Exception:
        return {"winner": "A", "reasons": ["fallback"]}
