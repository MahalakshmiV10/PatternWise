# AI Prompt Library

Part A contains **reusable templates** (not yet used by you). Part B is the record of what was **actually** used. Do not copy a template into Part B unless you really ran it. Replace `[PATTERN]` and other brackets with your own text.

## Part B: Actual-use record (keep this honest)

| # | Date | AI tool | Purpose | Prompt (summary) | Output summary | Verification performed | Errors / corrections |
|---|------|---------|---------|------------------|----------------|------------------------|----------------------|
| 1 | 2026-10-15 | Claude (Anthropic), chat | Generate the PatternWise project files from the CAPSTONE 73 master prompt | The full master prompt (project, folder tree, requirements) followed by "give all folders as a zip file" | Python code, tests, diagrams, docs, quiz, slide text | In the generation sandbox: ran the 8 examples and all unit tests with `python run_all.py`; broke code on purpose to confirm failure is reported. Details in `docs/ai_verification_report.md` | None observed in the sandbox run (this does not prove there are none) |
| 2 | [date] | [tool] | [purpose] | [your prompt] | [summary] | [what you checked] | [what was wrong] |

Add your own rows as you use AI tools. Institutions often require this disclosure.

## Part A: Templates (NOT YET USED)

Each template lists: purpose, tool field, prompt, and the fields to fill after use (output summary, verification, errors).

**T1. Researching a design pattern**
- Purpose: get a first explanation to compare with sources.
- AI tool used: [not yet used]
- Prompt: "Explain the [PATTERN] design pattern. Give its category, intent, problem, structure, when to use it, when NOT to use it, advantages, disadvantages, and cite sources I can open. If you are not sure about a fact or a URL, say so."
- After use: Output summary [ ] / Verification [open the cited pages] / Errors [ ]

**T2. Explaining a pattern to a beginner**
- Prompt: "Explain [PATTERN] to a third-year CSE student who is new to Python. Use simple English, one real-life analogy, and a tiny example. Avoid advanced syntax."

**T3. Generating Python code**
- Prompt: "Write a beginner-friendly Python 3 implementation of [PATTERN] using only the standard library. Include type hints, short comments, a demo() function, and input validation. Do not use ellipses or TODOs."

**T4. Reviewing code for correctness**
- Prompt: "Review this code for bugs, wrong use of the [PATTERN] pattern, and missing error handling. List each issue with the line and a fix. Do not claim to have run the code.\n[paste code]"

**T5. Designing UML diagrams**
- Prompt: "Write a Mermaid classDiagram for this code. Use only classes and methods that exist in the code. Explain every arrow.\n[paste code]"

**T6. Creating unit tests**
- Prompt: "Write Python unittest tests for this code: normal behaviour, edge cases, invalid input. No network access. Explain what each test proves.\n[paste code]"

**T7. Finding edge cases**
- Prompt: "List edge cases and failure cases for this [PATTERN] implementation (empty input, wrong types, repeated calls, shared state). Say which ones my tests do not cover.\n[paste code and tests]"

**T8. Comparing before-and-after**
- Prompt: "Show a short 'before' version without the [PATTERN] pattern and compare it with my 'after' version. Be honest about the extra complexity and say when the 'before' version is better."

**T9. Creating quiz questions**
- Prompt: "Write [N] multiple-choice questions on [PATTERNS]: scenario, code-understanding, pattern-selection and 'when NOT to use'. Exactly one defensible answer each, with a short explanation."

**T10. Preparing presentation slides**
- Prompt: "Create content for exactly seven slides with short bullets and speaker notes for: [slide titles]. Do not invent statistics or results."

**T11. Checking for hallucinations and outdated claims**
- Prompt: "List every factual claim in the text below (names, dates, URLs, library behaviour). For each, say how I can verify it and mark any you are unsure about.\n[paste text]"

**T12. Reviewing ethical issues**
- Prompt: "What ethical, privacy, security and academic-integrity issues exist in using AI to build and present this project? How should I disclose AI use?"
