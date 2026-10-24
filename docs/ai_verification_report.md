# AI Verification Report

## 1. Verification checklist (tick only what YOU have done)

- [ ] I ran `python run_all.py` on my own computer and saw `ALL CHECKS PASSED`.
- [ ] I ran it with the Python version I will submit with (`python --version`: ________).
- [ ] I opened every source in `research/sources.md`, confirmed it works, and filled in the date accessed.
- [ ] I cross-checked the pattern definitions with a second AI tool and recorded differences (Section 4).
- [ ] I rendered every diagram and completed the checklist in `diagrams/README.md`.
- [ ] I read every code file and can explain it.
- [ ] I ran the app (`python main.py`) and tried invalid input (letters, empty input, number 99).
- [ ] I ran the quiz (`python quiz/quiz.py`) and checked each answer and explanation.
- [ ] I followed my institution's AI-use and citation rules.
- [ ] I tested the Windows steps in the README from a clean folder.

## 2. Checks actually performed during project generation

Performed by Claude (Anthropic) in a Linux sandbox, **Python 3.12.3**, on 2026-10-15.

| Check | Result |
|-------|--------|
| `python run_all.py` (8 examples, `main.py --list`, all unit tests) | 10 of 10 checks passed, exit code 0 |
| Unit tests (`unittest discover`) | 103 tests, all passed |
| Failure detection: one price in `decorator.py` was temporarily changed (80 to 81) | `run_all.py` reported `[FAIL] Unit tests (all)`, summary `RESULT: FAILED`, exit code 1. Code was then restored and the run passed again (exit code 0) |
| Diagram name check (`tests/test_diagrams.py`) | Passed: every diagram class and method exists in the code, and every code class appears in the diagram |
| Demo outputs in `docs/pattern_notes.md` | Captured automatically from real runs |

## 3. Checks NOT performed (status: Not executed / not verified)

| Item | Status |
|------|--------|
| Python 3.14 | Not executed |
| Windows 10/11, PowerShell, `run_all.bat` | Not executed |
| VS Code settings, interpreter selection, launch configurations | Not executed |
| Rendering of Mermaid diagrams | Not executed |
| Opening and checking source URLs | Not executed (no internet in the sandbox) |
| Second AI tool cross-check | Not done |
| Thread safety of Singleton | Not tested |
| GitHub repository | Not created or uploaded |
| PowerPoint / PDF / image files | Not generated |

## 4. Issues found and corrected (template)

No bugs were observed in the sandbox runs. That does not prove none exist. Record your own findings here. Do not invent entries.

| # | Date | Where (file / claim) | What was wrong | How I found it | How I fixed it |
|---|------|----------------------|----------------|----------------|----------------|
| 1 | | | | | |
| 2 | | | | | |

## 5. Second-AI comparison (template)

| Pattern | Claim in my notes | What the second AI said | Which source decides | Final wording |
|---------|-------------------|--------------------------|----------------------|---------------|
| | | | | |
