# Ethics and Limitations

## Responsible AI use

1. **AI can produce plausible but wrong code.** Code that looks correct may fail. Run it and test it. This project's tests exist for that reason.
2. **AI diagrams may not match the code.** `tests/test_diagrams.py` checks class and method names, but you must still render and read each diagram.
3. **Sources must be verified.** AI can invent authors, URLs or quotations. Every source in `research/sources.md` is marked "needs verification" until you open it.
4. **AI must not be reported as having run what it did not run.** Only results from a real execution are recorded in `docs/testing_report.md`.
5. **Understand and present your work honestly.** You must be able to explain every file in your viva. Write your own words in the report and say which parts AI helped with.
6. **Follow your institution's rules** on AI use, citation and disclosure. Check them before submitting.
7. **Do not force a pattern.** See `docs/pattern_selection_checklist.md` and the "when NOT to use" sections.

## Security, privacy, maintainability, complexity

| Topic | Note |
|-------|------|
| Security | The core project needs no API keys, passwords or network. Never put secrets in the repository (`.gitignore` excludes `.env`). `run_all.py` only runs this project's own Python files with `subprocess` and never runs user input. |
| Privacy | No personal data is collected or stored. Do not add real names or IDs to the slide placeholders in a public repository unless you are comfortable with that. |
| Maintainability | Diagrams and docs can drift from the code. The diagram test catches some drift; update docs when you change code. |
| Complexity | Every pattern adds classes. The examples are deliberately small teaching examples. |

## Known limitations of this project

- **Python version:** requested Python 3.14. It was generated and tested only on Python 3.12.3. Nothing in the code is known to need 3.14, but it has **not** been run on 3.14 or on Windows. Run `python run_all.py` on your machine to find out.
- **Singleton** is not thread-safe, and this was not tested.
- **Observer:** if one observer raises an exception during `publish()`, later observers are not notified. This was not handled or tested.
- **Facade** does not stop direct use of subsystem classes.
- **Diagrams** are checked by name only and were not rendered during generation.
- **Sources** are unverified. **Second-AI cross-check** has not been done.
- **Quiz** has 15 questions. Questions were written with one intended answer, but you should read them critically; Q13 especially is a judgment question.
- The examples are simplified teaching models, not production code.
- Slides exist only as text (no `.pptx` file was generated).

## Future improvements

- Add more patterns (for example Command, State, Prototype).
- Add a thread-safe Singleton with a lock and tests for it.
- Add error handling for failing observers.
- Generate diagram images automatically (for example with Mermaid CLI, if you choose to install it).
- Add a GitHub Actions workflow that runs `python run_all.py`.
