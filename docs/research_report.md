# Research Report: Software Design Patterns Visual Guide

**Student:** [Your name] | **Roll number:** [ ] | **Institution:** [ ] | **Guide:** [ ] | **Date:** [ ]

## Abstract

This project builds an educational tool that explains eight software design patterns to third-year computer science students. For each pattern it provides a plain-English explanation, a real-life analogy, a Python implementation, a UML-style diagram, automated tests, and quiz questions. The project also studies how AI tools can help, and where they must be checked. Results reported here come only from checks that were actually run; items not yet checked are marked as such.

## 1. Introduction

A **design pattern** is a named, reusable solution to a problem that appears often in software design. The idea became widely known through the book by Gamma, Helm, Johnson and Vlissides (the "Gang of Four", S01). **UML** (Unified Modeling Language) is a way to draw classes and their relationships. **Unit tests** are small programs that check that parts of the code behave correctly.

## 2. Problem statement

Beginners often read pattern descriptions that are abstract, with diagrams that do not match code, and examples that are never run. AI tools can quickly produce explanations and code, but they can also produce plausible mistakes. The problem is how to use AI to explain patterns clearly while keeping the content correct and honest.

## 3. Objectives

1. Explain eight patterns in simple English with analogies.
2. Implement each in beginner-friendly Python.
3. Draw one diagram per pattern that matches the code.
4. Test every implementation automatically.
5. Provide a quiz and presentation material.
6. Document responsible AI use, verification, and when NOT to use a pattern.

## 4. Scope

**In scope:** eight patterns (3 creational, 3 structural, 2 behavioural), a command-line app, tests, diagrams, quiz, documents. **Out of scope:** all 23 GoF patterns, a graphical interface, web hosting, paid AI services, performance measurement.

## 5. Research methodology

1. Choose reference sources (S01-S19 in `research/sources.md`).
2. Draft explanations with AI help, using the prompt templates.
3. Compare AI output with sources and with a second AI tool.
4. Implement the code, then test it by running it.
5. Compare diagrams with code (automatic name check plus manual checklist).
6. Record issues in `docs/ai_verification_report.md`.

**Status:** steps 1 and 4 were done during generation; steps 2, 3 and the manual part of 5 are **to be completed by the student** (the sources were not opened and the second AI was not used).

## 6. Role of AI tools

AI helped to generate the code, tests, diagrams, quiz and drafts of the documents. AI is treated as an assistant whose output is a draft. Risks include plausible but wrong code, invented references, diagrams that differ from code, and false claims of having run tests (see `docs/ethics_and_limitations.md`).

## 7. Design pattern categories

| Category | Concern | Patterns here |
|----------|---------|---------------|
| Creational | How objects are created | Singleton, Factory Method, Builder |
| Structural | How objects are combined | Adapter, Decorator, Facade |
| Behavioural | How objects communicate and share work | Strategy, Observer |

## 8. Analysis of the eight patterns

| Pattern | One-line idea | Example here | Main caution |
|---------|---------------|--------------|--------------|
| Singleton | One shared instance | `AppConfig` | Hidden global state; hard to test |
| Factory Method | Subclass chooses the class | Email / SMS notifications | More classes |
| Builder | Build step by step | `PizzaBuilder` | Overkill for simple objects |
| Adapter | Convert an interface | Fahrenheit sensor to Celsius | Might hide a design that should be cleaned |
| Decorator | Wrap to add behaviour | Milk and sugar on espresso | Many small wrappers |
| Facade | One simple entry point | Home theater | Can grow into a "god class" |
| Strategy | Swappable algorithms | Shipping cost | Needless for one algorithm |
| Observer | Notify subscribers | News publisher | Forgotten unsubscribes; failing observers |

Full details: `docs/pattern_notes.md`.

## 9. Pattern selection checklist

See `docs/pattern_selection_checklist.md`. Main message: patterns are optional tools. Use one only when it removes a real problem and the added complexity is worth it.

## 10. Implementation approach

Standard library only; one file per pattern with a `demo()` function; type hints; short comments; input validation with clear exceptions; a menu app (`main.py`) that reads pattern information from `patterns/catalog.py`; `run_all.py` that runs all checks and returns a non-zero exit code on failure.

## 11. Testing methodology

`unittest`, repeatable, no network. Normal, edge and invalid cases per pattern. Test doubles for the Facade, scripted input for the menu and quiz. Details: `docs/testing_report.md`.

## 12. AI verification methodology

Run the code; compare diagrams with code; open each source; cross-check with a second tool; record real issues and corrections; never record a check that was not done. Template: `docs/ai_verification_report.md`.

## 13. Ethics and limitations

See `docs/ethics_and_limitations.md` (plausible-but-wrong output, honesty about AI use, institutional rules, security and privacy notes, Singleton and Observer limitations).

## 14. Results (based only on actual verification)

- All eight patterns implemented; each example runs.
- In the generation environment (Python 3.12.3, Linux): 103 unit tests ran and passed; `python run_all.py` passed 10 of 10 checks; a deliberate code change made it fail with exit code 1 as intended.
- Not yet verified: Python 3.14, Windows, diagram rendering, sources, second-AI cross-check.
- No performance or learning-effect measurements were made, so none are claimed.

[Student: replace or extend this section with your own run results.]

## 15. Conclusion

The project shows that AI can speed up producing explanations, code, tests and diagrams, but correctness comes from running the code, comparing diagrams with source, and checking references. Automated tests and a one-command check make some of that verification repeatable. The student remains responsible for understanding and honestly presenting the work.

## 16. References

All entries are in `research/sources.md` (S01-S19) and are **pending verification**. Cite them in your institution's required style only after opening and checking them. Main ones:

- S01: Gamma, E., Helm, R., Johnson, R., Vlissides, J. *Design Patterns: Elements of Reusable Object-Oriented Software.* Addison-Wesley, 1994.
- S02-S10: Refactoring.Guru design pattern pages.
- S11-S16: Python documentation (unittest, abc, dataclasses, data model, subprocess).
- S15: Mermaid class diagram documentation.
