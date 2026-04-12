# ALFA: Dead Agents, Living System

System agentów, który nie naprawia błędów.
Eliminuje martwe wzorce na zawsze i ewoluuje przez zastępowanie.

## Quick Start (v2)

```bash
pip install -e .
python app/main.py
```

Konfiguracja providera LLM przez zmienne środowiskowe:

```bash
# mock (domyślnie)
export MODEL_PROVIDER=mock
export MODEL_NAME=qwen2.5

# ollama
export MODEL_PROVIDER=ollama
export MODEL_NAME=qwen2.5

# openai
export MODEL_PROVIDER=openai
export MODEL_NAME=gpt-4.1-mini
export OPENAI_API_KEY=...
```

## Jak działa

- Krótki rynek planów: 2.5 min prezentacja + 2.5 min dowód przewagi.
- Duża głowa wybiera i stempluje najlepszy plan.
- Wykonanie idzie w krótkich, kontrolowanych odcinkach A -> B.
- ALFA Brain wstrzykuje tylko potrzebny fragment pamięci i kolejny slice.
- Cerber pilnuje zgodności na żywo.
- Guardian red-teamuje każdy raport niezależnie od wykonawcy.
- Łasuch rejestruje trupy i odkłada je do rejestru wzorców martwych.
- Martwe wzorce nigdy nie wracają.
- Druga drużyna non-stop buduje nowych agentów.
- System self-evolve zamiast self-heal.

## Jedno zdanie

Nie leczymy chorych agentów.
Uczymy się, jakich wzorców nigdy więcej nie budować.

## Big Model Wakes Only When Needed

W ALFA duży model nie działa stale podczas wykonania.
Budzi się tylko na checkpointach.

Przepływ:

1. Agent dochodzi do punktu B.
2. Agent melduje i zatrzymuje się.
3. Duży model czyta zweryfikowany stan od B do C.
4. Duży model waży decyzję i buduje kolejny krótki odcinek.
5. ALFA Brain zapisuje injection.
6. Wykonanie wraca do krótkiego agenta/slice.

Dlaczego to działa:

- Mniej halucynacji: brak długiej autonomii i driftu kontekstu.
- Mniej tokenów: duży model pracuje tylko na punktach decyzyjnych.
- Czysta odpowiedzialność: model decyduje, agent wykonuje.

Najmocniejsze zdanie:

The large model wakes only at control points, reads the next segment, injects the next step, and goes back to sleep.

## Final Truth Test

Na końcu program przechodzi przez szczere testy.
Nie testy pod pokaz, tylko testy, które naprawdę próbują go złamać.

Sprawdzamy:

1. Czy robi to, co miał robić: cel, przepływ, logika użytkownika.
2. Czy nie robi głupot: błędne akcje, martwe ścieżki, fałszywe sukcesy, niespójny stan.
3. Czy nie oszukuje wynikiem: raport, ślad i efekt muszą się zgadzać.

Jeśli zachowuje się głupio pod uczciwym testem:

- nie pudrujemy,
- nie tłumaczymy,
- nie łatamy na szybko,
- spalmy wzorzec i budujmy od nowa.

Hasło systemowe:

If it behaves stupidly under honest testing, burn the pattern and rebuild.

## Struktura repo

```text
/docs
	/architecture
		market-phase.md
		big-head.md
		alfa-brain.md
		cerber.md
		guardian.md
		lasuch.md
		dead-pattern-registry.md
		execution-slices.md
		team-bench-evolution.md
	/principles
		short-path-no-cheat.md
		dead-means-dead.md
		proposed-is-not-proven.md
```

## Inspiracje Red Teaming

- Guardian-style verification: niezależny, adwersarialny auditing ścieżek.
- Dead pattern burn: eliminacja porażek zamiast ich pudrowania.
- Live enforcement + final truth test: monitoring ciągły plus uczciwe testy łamiące.
- Short slices + checkpoint wake: mniejszy blast radius i mniejsza powierzchnia błędu.

ALFA wzmacnia to architektonicznie:

- Guardian jako wbudowany red team.
- Łasuch jako permanentny kill switch wzorców, które nie przechodzą prawdy.
