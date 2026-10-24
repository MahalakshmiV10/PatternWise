"""PatternWise quiz: 15 multiple-choice questions on the eight design patterns.

Run the quiz:                 python quiz/quiz.py
Rewrite quiz.md/answer_key.md: python quiz/quiz.py --export
"""
import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Optional

LETTERS = "ABCD"


@dataclass(frozen=True)
class Question:
    number: int
    kind: str  # Scenario, Code understanding, Pattern selection, When NOT to use
    text: str
    options: tuple[str, ...]
    answer_index: int  # 0 = A, 1 = B, ...
    explanation: str
    code: str = ""


QUESTIONS: tuple[Question, ...] = (
    Question(
        1, "Scenario",
        "A game needs exactly ONE shared settings object that every screen reads and updates. Which pattern fits best?",
        ("Singleton", "Builder", "Observer", "Adapter"), 0,
        "Singleton guarantees one instance with a global access point.",
    ),
    Question(
        2, "Scenario",
        "A base class has a method that must return a notification object. The Email subclass and the SMS subclass each decide which concrete class to create. Which pattern is this?",
        ("Strategy", "Decorator", "Factory Method", "Facade"), 2,
        "In Factory Method, subclasses override a creation method to choose the concrete product.",
    ),
    Question(
        3, "Scenario",
        "A constructor takes nine parameters, most of them optional, and calls like Pizza('large', None, None, True, None, ...) are hard to read. Which pattern helps?",
        ("Adapter", "Builder", "Singleton", "Observer"), 1,
        "Builder constructs an object step by step and lets you skip optional parts clearly.",
    ),
    Question(
        4, "Scenario",
        "Your app expects get_temperature_celsius(), but an old library you cannot edit only offers read_fahrenheit(). Which pattern fits?",
        ("Strategy", "Builder", "Singleton", "Adapter"), 3,
        "Adapter converts one interface into the interface the client expects.",
    ),
    Question(
        5, "Scenario",
        "Customers may add milk, sugar, or both to any drink, and the price must add up, without writing a subclass for every combination. Which pattern fits?",
        ("Decorator", "Factory Method", "Singleton", "Facade"), 0,
        "Decorator wraps an object to add behaviour, and wrappers can be stacked.",
    ),
    Question(
        6, "Scenario",
        "Starting a home theater needs a projector, an amplifier and a player, in the correct order. The client wants ONE simple call. Which pattern fits?",
        ("Observer", "Facade", "Adapter", "Builder"), 1,
        "Facade offers a simple interface to a group of subsystem classes.",
    ),
    Question(
        7, "Pattern selection",
        "A shop must switch between Standard, Express and Free shipping calculations at run time, using the same Order class. Which pattern fits?",
        ("Singleton", "Facade", "Strategy", "Adapter"), 2,
        "Strategy keeps interchangeable algorithms in separate classes that the context can swap.",
    ),
    Question(
        8, "Pattern selection",
        "When a publisher posts news, every subscriber must be informed automatically, and subscribers can leave at any time. Which pattern fits?",
        ("Strategy", "Facade", "Singleton", "Observer"), 3,
        "Observer defines a one-to-many dependency so subscribers are notified automatically.",
    ),
    Question(
        9, "Code understanding",
        "What does the program print?",
        ("True", "False", "An error is raised", "None"), 0,
        "AppConfig is a Singleton, so both variables refer to the same object and 'is' gives True.",
        code="first = AppConfig()\nsecond = AppConfig()\nprint(first is second)",
    ),
    Question(
        10, "Code understanding",
        "Espresso costs 80, MilkDecorator adds 20 and SugarDecorator adds 5. What does the program print?",
        ("100", "105", "125", "25"), 1,
        "80 + 20 + 5 = 105. Each decorator adds its price to the wrapped drink's price.",
        code="drink = SugarDecorator(MilkDecorator(Espresso()))\nprint(drink.cost())",
    ),
    Question(
        11, "Code understanding",
        "Two Subscriber objects, a and b, are attached. Then b is detached. How many subscribers receive 'Hi'?",
        ("0", "1", "2", "3"), 1,
        "Only a is still attached, so only a receives the message. publish() also returns 1.",
        code="publisher.attach(a)\npublisher.attach(b)\npublisher.detach(b)\npublisher.publish('Hi')",
    ),
    Question(
        12, "When NOT to use",
        "A program needs to convert kilometres to miles with one fixed formula that will never change. What is the best approach?",
        ("A Strategy class for each formula", "A Singleton converter object", "A simple function", "An Observer for the result"), 2,
        "One fixed formula needs no pattern. A plain function is simpler and easier to test.",
    ),
    Question(
        13, "When NOT to use",
        "Your shop will only ever use Standard shipping and no change is planned. Is the Strategy pattern needed?",
        ("Yes, always use Strategy for any calculation", "No, a simple method is enough until there are several interchangeable algorithms", "Yes, because Strategy is faster", "No, because Strategy only works for payments"), 1,
        "Patterns add classes and complexity. Use Strategy only when there are really several algorithms to swap.",
    ),
    Question(
        14, "Pattern selection",
        "Which list contains ONLY structural patterns?",
        ("Adapter, Decorator, Facade", "Singleton, Adapter, Facade", "Strategy, Observer, Decorator", "Builder, Facade, Adapter"), 0,
        "Adapter, Decorator and Facade are structural. Singleton and Builder are creational. Strategy and Observer are behavioural.",
    ),
    Question(
        15, "When NOT to use",
        "What is a common problem when many unit tests use a Singleton?",
        ("A Singleton cannot store data", "Data set by one test can stay and affect other tests", "A Singleton cannot be imported", "A Singleton makes Python crash"), 1,
        "The shared instance keeps its state between tests, so tests must reset it (like reset_instance() in this project).",
    ),
)


def parse_answer(text: str, option_count: int) -> Optional[int]:
    """Turn 'a', 'B', '3' ... into an option index. Return None if invalid."""
    cleaned = text.strip().upper()
    if len(cleaned) != 1:
        return None
    if cleaned in LETTERS[:option_count]:
        return LETTERS.index(cleaned)
    if cleaned.isdigit() and 1 <= int(cleaned) <= option_count:
        return int(cleaned) - 1
    return None


def run_quiz(
    input_fn: Callable[[str], str] = input,
    output_fn: Callable[[str], None] = print,
) -> tuple[int, int]:
    """Ask all questions. Returns (score, questions_answered)."""
    output_fn("\n=== PatternWise Quiz (15 questions) ===")
    output_fn("Type A, B, C or D (or 1-4). Type Q to stop early.\n")
    score = 0
    answered = 0
    for question in QUESTIONS:
        output_fn(f"Question {question.number} of {len(QUESTIONS)} [{question.kind}]")
        output_fn(question.text)
        if question.code:
            output_fn("")
            for line in question.code.splitlines():
                output_fn("    " + line)
            output_fn("")
        for index, option in enumerate(question.options):
            output_fn(f"  {LETTERS[index]}) {option}")

        choice: Optional[int] = None
        while choice is None:
            try:
                raw = input_fn("Your answer: ")
            except (EOFError, KeyboardInterrupt):
                raw = "q"
            if raw.strip().upper() == "Q":
                output_fn(f"\nQuiz stopped. Score: {score}/{answered} answered.")
                return score, answered
            choice = parse_answer(raw, len(question.options))
            if choice is None:
                output_fn("Invalid answer. Please type A, B, C or D.")

        answered += 1
        if choice == question.answer_index:
            score += 1
            output_fn("Correct!")
        else:
            correct_letter = LETTERS[question.answer_index]
            output_fn(f"Not quite. The correct answer is {correct_letter}.")
        output_fn(f"Why: {question.explanation}\n")

    output_fn(f"=== Final score: {score}/{answered} ===")
    return score, answered


def build_quiz_markdown() -> str:
    lines = ["# PatternWise Quiz", "", "Choose the best answer for each question. Answers are in `answer_key.md`.", ""]
    for question in QUESTIONS:
        lines.append(f"## Question {question.number} ({question.kind})")
        lines.append("")
        lines.append(question.text)
        lines.append("")
        if question.code:
            lines.extend(["```python", question.code, "```", ""])
        for index, option in enumerate(question.options):
            lines.append(f"- {LETTERS[index]}) {option}")
        lines.append("")
    return "\n".join(lines)


def build_answer_key_markdown() -> str:
    lines = ["# PatternWise Quiz: Answer Key", "", "| Q | Answer | Explanation |", "|---|--------|-------------|"]
    for question in QUESTIONS:
        letter = LETTERS[question.answer_index]
        answer_text = question.options[question.answer_index]
        lines.append(f"| {question.number} | {letter}) {answer_text} | {question.explanation} |")
    lines.append("")
    return "\n".join(lines)


def export_markdown(folder: Path) -> None:
    """Write quiz.md and answer_key.md so they always match the questions above."""
    (folder / "quiz.md").write_text(build_quiz_markdown(), encoding="utf-8")
    (folder / "answer_key.md").write_text(build_answer_key_markdown(), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="PatternWise quiz")
    parser.add_argument("--export", action="store_true", help="rewrite quiz.md and answer_key.md")
    args = parser.parse_args()
    if args.export:
        export_markdown(Path(__file__).resolve().parent)
        print("quiz.md and answer_key.md written.")
    else:
        run_quiz()


if __name__ == "__main__":
    main()
