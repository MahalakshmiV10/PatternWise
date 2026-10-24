# Sources

**Status of every entry: NEEDS VERIFICATION.**
These sources were chosen because they are well-known references for the topics. They were **not opened or checked** when this project was generated (the generation environment had no internet access). URLs are written from memory of standard site layouts. Open each one, confirm it works and supports the claim, then fill in "Date accessed" and change the status.

Reliability scale: **Primary** (original or official), **Reputable secondary** (well-regarded explanation), **Tool docs** (official docs of a tool).

| ID | Title | Author / organisation | URL | Supports | Reliability (expected) | Date accessed | Status |
|----|-------|-----------------------|-----|----------|------------------------|---------------|--------|
| S01 | *Design Patterns: Elements of Reusable Object-Oriented Software* (book, 1994) | Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides; Addison-Wesley | (book, no URL) | Original definitions and categories of all eight patterns | Primary | [fill in] | Needs verification |
| S02 | Design Patterns catalog | Refactoring.Guru | https://refactoring.guru/design-patterns | Overview of categories and pattern list | Reputable secondary | [fill in] | Needs verification |
| S03 | Singleton | Refactoring.Guru | https://refactoring.guru/design-patterns/singleton | Singleton definition, pros, cons | Reputable secondary | [fill in] | Needs verification |
| S04 | Factory Method | Refactoring.Guru | https://refactoring.guru/design-patterns/factory-method | Factory Method definition, pros, cons | Reputable secondary | [fill in] | Needs verification |
| S05 | Builder | Refactoring.Guru | https://refactoring.guru/design-patterns/builder | Builder definition, pros, cons | Reputable secondary | [fill in] | Needs verification |
| S06 | Adapter | Refactoring.Guru | https://refactoring.guru/design-patterns/adapter | Adapter definition, pros, cons | Reputable secondary | [fill in] | Needs verification |
| S07 | Decorator | Refactoring.Guru | https://refactoring.guru/design-patterns/decorator | Decorator definition, pros, cons | Reputable secondary | [fill in] | Needs verification |
| S08 | Facade | Refactoring.Guru | https://refactoring.guru/design-patterns/facade | Facade definition, pros, cons | Reputable secondary | [fill in] | Needs verification |
| S09 | Strategy | Refactoring.Guru | https://refactoring.guru/design-patterns/strategy | Strategy definition, pros, cons | Reputable secondary | [fill in] | Needs verification |
| S10 | Observer | Refactoring.Guru | https://refactoring.guru/design-patterns/observer | Observer definition, pros, cons | Reputable secondary | [fill in] | Needs verification |
| S11 | unittest - Unit testing framework | Python Software Foundation | https://docs.python.org/3/library/unittest.html | How tests, `setUp`, `assertRaises`, discovery work | Tool docs | [fill in] | Needs verification |
| S12 | abc - Abstract Base Classes | Python Software Foundation | https://docs.python.org/3/library/abc.html | `ABC`, `@abstractmethod`, `TypeError` on abstract instantiation | Tool docs | [fill in] | Needs verification |
| S13 | dataclasses | Python Software Foundation | https://docs.python.org/3/library/dataclasses.html | `@dataclass(frozen=True)` used for `Pizza` and `PatternInfo` | Tool docs | [fill in] | Needs verification |
| S14 | Python data model (`__new__`) | Python Software Foundation | https://docs.python.org/3/reference/datamodel.html | `__new__` vs `__init__` (Singleton) | Tool docs | [fill in] | Needs verification |
| S15 | Mermaid: Class diagrams | Mermaid project | https://mermaid.js.org/syntax/classDiagram.html | Diagram syntax and arrow meanings | Tool docs | [fill in] | Needs verification |
| S16 | subprocess | Python Software Foundation | https://docs.python.org/3/library/subprocess.html | How `run_all.py` runs commands and reads exit codes | Tool docs | [fill in] | Needs verification |
| S17 | venv - Creation of virtual environments | Python Software Foundation | https://docs.python.org/3/library/venv.html | Virtual environment setup in README | Tool docs | [fill in] | Needs verification |
| S18 | Python environments in VS Code | Microsoft | https://code.visualstudio.com/docs/python/environments | Selecting the interpreter in VS Code | Tool docs | [fill in] | Needs verification |
| S19 | Creating a new repository | GitHub Docs | https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository | GitHub steps in README | Tool docs | [fill in] | Needs verification |

## Facts versus AI suggestions

| Kind | Examples in this project | How to treat it |
|------|--------------------------|-----------------|
| Fact to confirm from a source | Official pattern names and categories; what each pattern is meant to do (S01, S02-S10); how `unittest`, `abc`, `dataclasses`, `__new__` work (S11-S14); Mermaid arrow meanings (S15) | Open the source and confirm before submitting |
| AI-generated suggestion | The analogies (school principal, hotel desk, pizza, travel plug, coffee, remote, shipping, YouTube), the example domains, the "when NOT to use" lists, the quiz questions, the before/after snippets | Review critically; they are teaching choices, not facts from a source |
| Verified by running code | Demo outputs, test results (see `docs/testing_report.md`) | Re-run on your own computer |

## Cross-checking with a second AI tool

The project asks for at least two AI tools. **Not done yet.** To do it: paste the "Researching a design pattern" prompt from `research/ai_prompt_library.md` into a second tool (for example Gemini or ChatGPT), compare its answer with S01-S10, and record differences in `docs/ai_verification_report.md`.
