"""PatternWise: a command-line guide to eight software design patterns.

Start the app:        python main.py
List the patterns:    python main.py --list
Run one example:      python main.py --demo 3
"""
import argparse
import importlib
from collections.abc import Callable

from patterns.catalog import PATTERNS, PatternInfo, get_pattern, patterns_by_category
from quiz.quiz import run_quiz

InputFn = Callable[[str], str]


def read_input(prompt: str, input_fn: InputFn = input) -> str | None:
    """Read one line. Returns None if input is closed (Ctrl+Z / Ctrl+C)."""
    try:
        return input_fn(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        return None


def show_welcome() -> None:
    print("=" * 56)
    print("  PatternWise - Software Design Patterns Visual Guide")
    print("=" * 56)
    print("Learn 8 design patterns with analogies, code and tests.")


def show_all_patterns() -> None:
    print("\nThe eight patterns, grouped by category:")
    for category, items in patterns_by_category().items():
        print(f"\n  {category}")
        for info in items:
            print(f"    {info.number}. {info.name:<15} - {info.purpose}")


def show_menu() -> None:
    print("\nMenu")
    print("  1-8  Learn a pattern and run its example")
    print("  A    Show all patterns")
    print("  Q    Take the quiz")
    print("  X    Exit")


def show_pattern_details(info: PatternInfo) -> None:
    print(f"\n{info.name} ({info.category})")
    print("-" * 40)
    print("Purpose :", info.purpose)
    print("Analogy :", info.analogy)
    print("Use case:", info.use_case)


def run_demo(info: PatternInfo) -> bool:
    """Run the demo() of a pattern module. Returns True on success."""
    print(f"\nRunning the {info.name} example...\n")
    try:
        module = importlib.import_module(info.module)
        module.demo()
        return True
    except Exception as error:  # show a friendly message instead of crashing  # noqa: BLE001
        print(f"Sorry, the example could not run: {error}")
        return False


def handle_choice(choice: str, input_fn: InputFn = input) -> bool:
    """Act on one menu choice. Returns False when the user wants to exit."""
    command = choice.strip().upper()
    if command in ("X", "EXIT"):
        return False
    if command == "":
        print("Please type a menu choice (for example 1, A, Q or X).")
    elif command == "A":
        show_all_patterns()
    elif command == "Q":
        run_quiz(input_fn)
    elif command.isdigit():
        info = get_pattern(int(command))
        if info is None:
            print(f"Invalid number '{choice}'. Please choose 1 to {len(PATTERNS)}.")
        else:
            show_pattern_details(info)
            run_demo(info)
            read_input("\nPress Enter to return to the menu...", input_fn)
    else:
        print(f"Invalid choice '{choice}'. Please use 1-8, A, Q or X.")
    return True


def run_menu(input_fn: InputFn = input) -> None:
    show_welcome()
    show_all_patterns()
    while True:
        show_menu()
        choice = read_input("\nYour choice: ", input_fn)
        if choice is None or not handle_choice(choice, input_fn):
            print("\nGoodbye! Good luck with your viva.")
            return


def main(argv: list[str] | None = None, input_fn: InputFn = input) -> int:
    parser = argparse.ArgumentParser(description="PatternWise design patterns guide")
    parser.add_argument("--list", action="store_true", help="list the patterns and exit")
    parser.add_argument("--demo", type=int, metavar="N", help="run the example of pattern N (1-8)")
    args = parser.parse_args(argv)

    if args.list:
        show_all_patterns()
        return 0
    if args.demo is not None:
        info = get_pattern(args.demo)
        if info is None:
            print(f"Invalid pattern number {args.demo}. Please choose 1 to {len(PATTERNS)}.")
            return 2
        return 0 if run_demo(info) else 1
    run_menu(input_fn)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
