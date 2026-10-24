# Slide Content (exactly 7 slides)

**Status:** text only. No `.pptx` file has been generated. To make slides: open PowerPoint or Google Slides, create 7 slides, paste the title and bullets, and add the suggested visuals. Take screenshots yourself from your own run.

---

## Slide 1: Title and Introduction

- **PatternWise: Software Design Patterns Visual Guide** (CAPSTONE 73)
- Student: [Name] | Roll no.: [ ] | Department: CSE | Year: 3rd
- Guide: [Name] | Institution: [ ] | Date: [ ]
- Question: How can AI help explain design patterns with clear diagrams and tested code?
- *Visual:* project title banner or screenshot of the welcome screen (`python main.py`).

## Slide 2: Problem, Objectives, Methodology

- Problem: pattern explanations are abstract; AI output can be wrong
- Objectives: explain 8 patterns, run the code, draw diagrams, test, quiz
- Method: sources, AI drafts, implement, test, compare diagrams, record issues
- Rule: verify everything AI produces
- *Visual:* simple 5-step flow (Research, Code, Test, Diagram, Verify).

## Slide 3: Pattern Overview

- Creational (creating objects): Singleton, Factory Method, Builder
- Structural (combining objects): Adapter, Decorator, Facade
- Behavioural (object communication): Strategy, Observer
- Patterns are optional tools, not rules
- *Visual:* three-column table of the categories.

## Slide 4: Selected Patterns and Examples

- Singleton: one shared `AppConfig`
- Factory Method: Email or SMS notification chosen by subclass
- Builder: pizza built step by step
- Adapter: Fahrenheit sensor used as Celsius
- Decorator: espresso + milk + sugar = Rs 105
- Facade: `watch_movie()` starts everything
- Strategy: Standard / Express / Free shipping
- Observer: subscribers notified, unsubscribed ones are not
- *Visual:* screenshot of one demo output (use real output from `docs/pattern_notes.md` or your own run).

## Slide 5: Architecture, UML, Implementation

- Folders: `patterns/`, `tests/`, `diagrams/`, `docs/`, `quiz/`
- `main.py` menu reads `patterns/catalog.py` and runs each `demo()`
- Python standard library only; no API keys
- One Mermaid diagram per pattern; names checked against code
- *Visual:* rendered `decorator.mmd` or `strategy.mmd` and the folder tree.

## Slide 6: Testing, Automation, AI Verification, Responsible AI

- `unittest` tests for every pattern, plus app, quiz and diagram checks
- `python run_all.py`: runs examples and tests, exits non-zero on failure
- AI can be plausibly wrong: run, compare, cite, disclose
- Sources must be opened and checked
- *Visual:* screenshot of your own `run_all.py` summary.

## Slide 7: Results, Limitations, Conclusion, Future Work

- Results: [your own numbers from your run; do not copy numbers you did not see]
- Limitations: simple examples; Singleton not thread-safe; diagrams checked by name; some checks pending
- Conclusion: AI speeds up drafting; testing and verification make it trustworthy
- Future: more patterns, thread-safe Singleton, automatic diagram images, CI
- *Visual:* summary table of done vs. pending checks.
