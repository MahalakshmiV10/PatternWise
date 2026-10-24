# Final Demo Script (about 5 minutes)

Practise this before the viva. Run every command yourself first so nothing surprises you.

| Time | What to do | What to say |
|------|------------|-------------|
| 0:00 | Open the folder in VS Code. Show the folder tree. | "PatternWise has patterns, tests, diagrams, docs, a quiz and slides." |
| 0:30 | Terminal: `python main.py` | "This is the learning app. Patterns are grouped by category." |
| 1:00 | Type `1`, then Enter. Then Enter again to return. | "It shows purpose, analogy and use case, then runs the example." |
| 1:45 | Type `abc`, then `99`. | "Invalid input gives a message and does not crash." |
| 2:00 | Type `7` (Strategy). Open `diagrams/strategy.mmd` preview. | "The diagram matches `strategy.py`: an abstract strategy, three concrete ones, and Order using it." |
| 2:45 | Type `q` and answer two questions, then `q` to stop. | "The quiz gives feedback and explanations." |
| 3:15 | Type `x`. Run `python run_all.py`. | "One command runs all eight examples and all tests." |
| 4:00 | Point to the summary. | "It prints PASS or FAIL per check and exits with a non-zero code if anything fails." |
| 4:30 | Open `docs/ethics_and_limitations.md`. | "AI helped draft; I verified it. These are the limits." |

## Backup plan

- If the app will not start: show `python -m patterns.creational.singleton` and the README troubleshooting section.
- If a test fails live: read the failing test name, say what it checks, and open the code. Do not guess.

## Only say things that are true

Report the actual number of tests and the actual result from your own run of `python run_all.py`.
