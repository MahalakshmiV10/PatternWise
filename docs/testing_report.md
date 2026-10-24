# Testing Report

## Actual result of the last run (done during project generation)

- Command: `python -m unittest discover -s tests -t . -v`
- Environment: Linux sandbox, **Python 3.12.3** (not Python 3.14, not Windows)
- Result: **Ran 103 tests in 1.096s, final line: `OK`**
- Not passed: 0

| Test file | Tests run | Passed | What it checks |
|-----------|-----------|--------|----------------|
| `test_adapter.py` | 9 | 9 | 212 F = 100 C, 32 F = 0 C, -40 equal, 98.6 F about 37 C; target interface satisfied; below-absolute-zero rejected; legacy unchanged. |
| `test_app.py` | 12 | 12 | Catalog has 8 patterns; every module has demo(); menu survives invalid input; --list and --demo options; quiz reachable from menu. |
| `test_builder.py` | 10 | 10 | Defaults; full chain; size required; invalid size/crust/topping rejected; built object isolated and immutable. |
| `test_decorator.py` | 9 | 9 | Base cost kept; add-ons add price and text; stacking and order; wrapped object unchanged; wrong type rejected. |
| `test_diagrams.py` | 4 | 4 | Diagram classes and methods exist in code; every code class appears in its diagram. |
| `test_facade.py` | 8 | 8 | Subsystem call order recorded with test doubles; return messages; end without start fails; empty title starts nothing. |
| `test_factory_method.py` | 7 | 7 | Correct concrete class per creator; channel text; empty/whitespace message rejected; abstract classes not instantiable. |
| `test_observer.py` | 9 | 9 | All subscribers notified; detached one stops; duplicates ignored; unknown detach fails; order preserved. |
| `test_quiz.py` | 12 | 12 | 15 well-formed questions; code answers match real program results; invalid input retried; quiz.md matches quiz.py. |
| `test_run_all.py` | 7 | 7 | run_all reports pass for exit 0, fail for exit 3, crash, missing program, timeout; summary exit code. |
| `test_singleton.py` | 6 | 6 | Same object returned; shared state; default value; empty key rejected; reset gives a fresh object (state isolation). |
| `test_strategy.py` | 9 | 9 | 70 / 175 / 0 for 2.5 kg; swap at run time; round-up of weight; invalid weight and strategy rejected. |

Also executed: `python run_all.py` gave 10 of 10 checks passed (8 examples, `main.py --list`, unit tests), exit code 0.

## Not executed

| Item | Status |
|------|--------|
| Tests on Python 3.14 | Not executed |
| Tests on Windows | Not executed |
| Tests under pytest | Not executed (project uses `unittest` only) |
| Multi-threaded tests (Singleton, Observer) | Not executed (no such tests exist) |

**Your task:** run `python run_all.py` on your computer and replace the lines above with your own numbers and Python version.

## Methodology

- One framework: Python `unittest` (standard library).
- No network access, no files written, no external APIs in tests.
- Tests are repeatable: the Singleton is reset in `setUp`/`tearDown`; Facade tests use recording subclasses instead of real devices; interactive menu and quiz tests use scripted input.
- Each pattern has normal cases, edge cases, and invalid-input cases.
- A deliberate-failure check was done once: changing one price made the suite fail and `run_all.py` exit with code 1 (see `docs/ai_verification_report.md`).

## Test design notes

- **Singleton:** shared state would leak between tests, so every test resets the instance.
- **Factory Method:** checks the concrete class with `assertIsInstance`.
- **Builder:** checks defaults, optional parts, validation and the final object.
- **Adapter:** checks the target interface works and the legacy object is unchanged.
- **Decorator:** checks original behaviour is kept and added behaviour appears.
- **Facade:** checks the order of subsystem calls.
- **Strategy:** checks different strategies give different expected results.
- **Observer:** checks notifications arrive, and that unsubscribed observers do not receive later ones.
- Quiz answers for code questions are computed by running the real code in the test.

## Limits of these tests

Passing tests show the checked behaviour works. They do not prove the code is free of bugs, and diagram tests do not prove diagrams render.
