"""Tests for the pattern catalog and the command-line app (main.py)."""
import contextlib
import importlib
import io
import unittest
from typing import Iterable

import main
from patterns.catalog import CATEGORIES, PATTERNS, get_pattern, patterns_by_category


def scripted_input(answers: Iterable[str]):
    """Return an input() replacement that gives the answers one by one."""
    iterator = iter(answers)

    def fake_input(prompt: str = "") -> str:
        try:
            return next(iterator)
        except StopIteration:
            raise EOFError from None

    return fake_input


def capture(function, *args, **kwargs) -> str:
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        function(*args, **kwargs)
    return buffer.getvalue()


class TestCatalog(unittest.TestCase):
    def test_there_are_eight_unique_numbered_patterns(self) -> None:
        self.assertEqual([info.number for info in PATTERNS], list(range(1, 9)))
        self.assertEqual(len({info.name for info in PATTERNS}), 8)

    def test_every_module_has_a_demo_function(self) -> None:
        for info in PATTERNS:
            module = importlib.import_module(info.module)
            self.assertTrue(callable(getattr(module, "demo", None)), info.name)

    def test_category_grouping(self) -> None:
        grouped = patterns_by_category()
        self.assertEqual(tuple(grouped), CATEGORIES)
        self.assertEqual([len(grouped[name]) for name in CATEGORIES], [3, 3, 2])

    def test_unknown_pattern_number(self) -> None:
        self.assertIsNone(get_pattern(99))
        self.assertIsNone(get_pattern(0))


class TestMainApp(unittest.TestCase):
    def test_list_option(self) -> None:
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            code = main.main(["--list"])
        self.assertEqual(code, 0)
        self.assertIn("Singleton", buffer.getvalue())
        self.assertIn("Observer", buffer.getvalue())

    def test_demo_option_runs_an_example(self) -> None:
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            code = main.main(["--demo", "1"])
        self.assertEqual(code, 0)
        self.assertIn("Same object? True", buffer.getvalue())

    def test_demo_option_with_invalid_number(self) -> None:
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            code = main.main(["--demo", "99"])
        self.assertEqual(code, 2)
        self.assertIn("Invalid pattern number", buffer.getvalue())

    def test_menu_survives_invalid_input(self) -> None:
        answers = ["abc", "99", "", "-1", "1", "", "x"]
        output = capture(main.run_menu, scripted_input(answers))
        self.assertIn("Invalid choice 'abc'", output)
        self.assertIn("Invalid number '99'", output)
        self.assertIn("Please type a menu choice", output)
        self.assertIn("Singleton (Creational)", output)
        self.assertIn("Goodbye", output)

    def test_menu_exits_cleanly_when_input_closes(self) -> None:
        output = capture(main.run_menu, scripted_input([]))
        self.assertIn("Goodbye", output)

    def test_menu_can_run_every_pattern(self) -> None:
        answers = []
        for number in range(1, 9):
            answers.extend([str(number), ""])
        answers.append("x")
        output = capture(main.run_menu, scripted_input(answers))
        for info in PATTERNS:
            self.assertIn(f"{info.name} (", output)

    def test_menu_can_start_the_quiz(self) -> None:
        output = capture(main.run_menu, scripted_input(["q", "q", "x"]))
        self.assertIn("PatternWise Quiz", output)
        self.assertIn("Quiz stopped", output)

    def test_read_input_returns_none_on_eof(self) -> None:
        self.assertIsNone(main.read_input("> ", scripted_input([])))


if __name__ == "__main__":
    unittest.main()
