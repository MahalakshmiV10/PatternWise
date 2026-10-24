# Project Overview: PatternWise (CAPSTONE 73)

**Title:** Software Design Patterns Visual Guide
**Question:** How can AI help explain design patterns with clear diagrams and tested code?
**Audience:** Third-year CSE students.

## What the project contains

| Part | Where |
|------|-------|
| Eight pattern implementations | `patterns/` |
| Pattern information used by the menu | `patterns/catalog.py` |
| Command-line learning app | `main.py` |
| One-command verification | `run_all.py`, `run_all.bat` |
| Unit tests | `tests/` |
| Mermaid diagrams | `diagrams/` |
| Reports and notes | `docs/` |
| Sources and prompt library | `research/` |
| Quiz (15 questions) | `quiz/` |
| Slide text (7 slides) and speaker notes | `presentation/` |

## The eight patterns

| Category | Patterns |
|----------|----------|
| Creational | Singleton, Factory Method, Builder |
| Structural | Adapter, Decorator, Facade |
| Behavioural | Strategy, Observer |

## How the parts connect

```
main.py  --reads-->  patterns/catalog.py  --imports-->  patterns/<category>/<pattern>.py (demo())
   |                                                       ^
   +--> quiz/quiz.py                                       |
run_all.py --runs--> each pattern demo + main.py --list + unit tests (tests/)
tests/test_diagrams.py --compares--> diagrams/*.mmd with the pattern classes
```

## Design decisions

- **Standard library only.** No packages to install, no API keys.
- **Every pattern file has a `demo()` function** and can run alone with `python -m patterns.<category>.<name>`.
- **Quiz markdown is generated from `quiz/quiz.py`**, so `quiz.md` and `answer_key.md` cannot disagree with the quiz that runs. A test checks this.
- **Money is stored as whole rupees (integers)** to avoid floating-point rounding surprises.
- **Folder name `behavioural`** (British spelling) follows the project brief.
- **Extra files added beyond the required structure:** `patterns/catalog.py`, `quiz/__init__.py`, `tests/test_app.py`, `tests/test_quiz.py`, `tests/test_run_all.py`, `tests/test_diagrams.py`.
