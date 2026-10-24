# PatternWise: Software Design Patterns Visual Guide (CAPSTONE 73)

A beginner-friendly command-line project that explains eight software design patterns with analogies, Python code, diagrams, tests, a quiz, and presentation material.

> **Honest status:** generated and tested on Linux with Python 3.12.3. It has **not yet been run on Windows or Python 3.14**. Run `python run_all.py` on your computer first (see section 9) and record your own result.

## 1. Features

- Menu app: list patterns by category, see purpose, analogy and use case, run each example
- 8 runnable examples: Singleton, Factory Method, Builder, Adapter, Decorator, Facade, Strategy, Observer
- 8 Mermaid diagrams in `diagrams/`
- Unit tests (`unittest`) for every pattern, the app, the quiz, `run_all.py` and the diagrams
- 15-question quiz with explanations
- One command to check everything: `python run_all.py`
- Reports, research notes, slide text and viva questions in `docs/`, `research/`, `presentation/`
- Python standard library only. No API keys, no paid services

## 2. Folder structure

```
PatternWise/
├── README.md, requirements.txt, .gitignore, LICENSE
├── main.py              menu app
├── run_all.py           runs every check
├── run_all.bat          Windows shortcut for run_all.py
├── patterns/            catalog.py + creational/ structural/ behavioural/
├── tests/               unit tests
├── diagrams/            Mermaid .mmd files + how to render
├── docs/                reports, notes, checklists, viva, demo script
├── research/            sources.md, ai_prompt_library.md
├── quiz/                quiz.py, quiz.md, answer_key.md
├── presentation/        slide_content.md, speaker_notes.md
└── .vscode/             settings.json, launch.json
```

## 3. Prerequisites

- Windows 10 or 11
- Python 3 from https://www.python.org/downloads/ (the brief asks for Python 3.14; any recent Python 3 should work for this code, but only 3.12.3 has been tested). During installation, tick **"Add python.exe to PATH"**.
- Visual Studio Code from https://code.visualstudio.com/ with the **Python** extension (by Microsoft)

Check Python in PowerShell:

```powershell
python --version
```

It should print a version such as `Python 3.14.x`. If it says "not recognized", see Troubleshooting.

## 4. Windows setup (step by step)

Open the project folder in VS Code (**File > Open Folder**), then open a terminal (**Terminal > New Terminal**). It opens in the project folder.

**Step 1: create a virtual environment** (a private Python copy for this project)

```powershell
python -m venv .venv
```

**Step 2: activate it**

```powershell
.venv\Scripts\Activate.ps1
```

You should see `(.venv)` at the start of the line. If PowerShell blocks the script, run this once for the current window and try again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

**Step 3: install requirements** (this project has none, but the file exists)

```powershell
pip install -r requirements.txt
```

**Step 4: select the interpreter in VS Code**

1. Press `Ctrl+Shift+P`.
2. Type **Python: Select Interpreter** and press Enter.
3. Choose the one that shows `.venv` (path ending in `.venv\Scripts\python.exe`).

## 5. Run the application

```powershell
python main.py
```

Menu: `1`-`8` learn a pattern and run its example, `A` show all patterns, `Q` quiz, `X` exit. Wrong input (letters, empty, `99`) shows a message and the menu returns.

Other options:

```powershell
python main.py --list        # print the patterns and exit
python main.py --demo 5      # run pattern 5 (Decorator) only
```

## 6. Run individual examples

Run from the project root folder (the folder that contains `main.py`):

```powershell
python -m patterns.creational.singleton
python -m patterns.creational.factory_method
python -m patterns.creational.builder
python -m patterns.structural.adapter
python -m patterns.structural.decorator
python -m patterns.structural.facade
python -m patterns.behavioural.strategy
python -m patterns.behavioural.observer
```

`python -m` runs a file as part of a package so imports work. Expected output for each is in `docs/pattern_notes.md`.

## 7. Run unit tests

```powershell
python -m unittest discover -s tests -t . -v
```

- `discover` finds all `test_*.py` files; `-s tests` is where; `-t .` sets the project root; `-v` lists each test.
- One file only: `python -m unittest tests.test_observer -v`
- In VS Code you can also use the Testing panel (the flask icon); `.vscode/settings.json` already configures `unittest`.

## 8. Quiz

```powershell
python quiz/quiz.py
```

Answer with `A`-`D` (or `1`-`4`). `Q` stops early. Questions are in `quiz/quiz.py`. If you edit them, rewrite the markdown files with `python quiz/quiz.py --export` (a test checks they match).

## 9. Run all checks with one command

```powershell
python run_all.py
```

It runs the 8 examples, `main.py --list`, and all unit tests, prints PASS/FAIL for each, and ends with a summary. The exit code is `0` only if everything passed, otherwise `1`. Check it in PowerShell:

```powershell
echo $LASTEXITCODE
```

Windows shortcut: double-click `run_all.bat` or run `.\run_all.bat`.

## 10. Render the diagrams

See `diagrams/README.md`. Quick way: open https://mermaid.live and paste a `.mmd` file. Or install a Mermaid preview extension in VS Code. The diagrams were **not rendered** during generation; look at each one and complete the checklist.

## 11. Troubleshooting

| Problem | Fix |
|---------|-----|
| `'python' is not recognized` | Reinstall Python and tick "Add python.exe to PATH", or try `py --version` and use `py` instead of `python`. Restart the terminal. |
| `ModuleNotFoundError: No module named 'patterns'` | You are not in the project root. Run `cd` into the folder containing `main.py`, then use `python -m ...` commands from section 6. |
| Cannot activate `.venv` (script disabled) | Run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`, then activate again. |
| VS Code uses the wrong Python | `Ctrl+Shift+P` > Python: Select Interpreter > choose `.venv`. |
| `python run_all.py` shows `FAIL` | Read the "output of failed check" text printed under it. Fix that file and run again. Do not ignore a FAIL. |
| Tests are not found in VS Code | Run the command in section 7 in the terminal; then use "Python: Configure Tests" and choose unittest, folder `tests`. |
| Strange characters in output | The code prints plain ASCII only. If you see odd characters, run `chcp 65001` first. |

## 12. AI usage and verification notes

- AI (Claude, by Anthropic) generated the files from the CAPSTONE 73 brief. See `research/ai_prompt_library.md`.
- Verified in the generation sandbox: all unit tests and examples ran and passed on Python 3.12.3. Details and the list of **not verified** items: `docs/ai_verification_report.md`.
- Sources in `research/sources.md` are **unverified** until you open them.
- You must understand, test and honestly disclose your own use of AI, following your institution's rules. See `docs/ethics_and_limitations.md`.

## 13. Limitations and future improvements

See `docs/ethics_and_limitations.md`. Main points: simple teaching examples, Singleton not thread-safe, diagrams checked by name only, slides are text only (no `.pptx` generated), Windows and Python 3.14 untested.

## 14. GitHub: create a repository and push

Install Git from https://git-scm.com/download/win, and create a free GitHub account.

```powershell
git --version
git init
git add .
git status
git commit -m "Add PatternWise project"
```

- `git init` starts tracking this folder. `git add .` stages all files (`.gitignore` excludes `.venv` and caches). `git status` shows what will be saved. `git commit` saves a snapshot.
- Check that `git status` does not list `.venv/`, `__pycache__/` or any secret before committing.

Create the repository: on github.com click **New repository**, name it `PatternWise`, do **not** tick "Add a README", click **Create**. Then copy the commands GitHub shows. They look like this (replace `YOUR-USERNAME`):

```powershell
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/PatternWise.git
git push -u origin main
```

Suggested commits (optional, if you want a clean history): `Add project configuration and menu app`, `Add eight pattern implementations`, `Add unit tests and run_all script`, `Add Mermaid diagrams`, `Add documentation, quiz and presentation notes`.

> The repository has **not** been created or uploaded by this project. Only you can do that.

## 15. Before you submit

Complete the checklist in `docs/ai_verification_report.md` and fill in the placeholders (`[Your Name]`, `[fill in]`) in `LICENSE`, `research/`, `docs/research_report.md` and `presentation/slide_content.md`.

## Web app (Flask)
1. `pip install -r requirements.txt` (or double-click `run.bat` on Windows)
2. `python app.py` then open http://127.0.0.1:5000
3. Web tests: `python -m unittest discover -s tests_web -t .`
Progress is saved in your browser's localStorage only (not synced).
