"""Checks that run_all.py reports success and failure honestly."""
import sys
import unittest

import run_all


class TestRunAll(unittest.TestCase):
    def test_successful_command_is_reported_as_pass(self) -> None:
        result = run_all.run_check("ok", [sys.executable, "-c", "print('hello')"])
        self.assertTrue(result.passed)
        self.assertIn("hello", result.output)

    def test_failing_command_is_reported_as_fail(self) -> None:
        result = run_all.run_check("bad", [sys.executable, "-c", "import sys; sys.exit(3)"])
        self.assertFalse(result.passed)
        self.assertIn("exit code 3", result.detail)

    def test_crashing_command_is_reported_as_fail(self) -> None:
        result = run_all.run_check("crash", [sys.executable, "-c", "raise RuntimeError('boom')"])
        self.assertFalse(result.passed)
        self.assertIn("boom", result.output)

    def test_missing_program_is_reported_as_fail(self) -> None:
        result = run_all.run_check("missing", ["definitely-not-a-real-program-xyz"])
        self.assertFalse(result.passed)

    def test_timeout_is_reported_as_fail(self) -> None:
        result = run_all.run_check(
            "slow", [sys.executable, "-c", "import time; time.sleep(5)"], timeout=1
        )
        self.assertFalse(result.passed)
        self.assertIn("timed out", result.detail)

    def test_summary_exit_code(self) -> None:
        good = run_all.CheckResult("a", True, 0.1, "", "exit code 0")
        bad = run_all.CheckResult("b", False, 0.1, "", "exit code 1")
        self.assertEqual(run_all.print_summary([good]), 0)
        self.assertEqual(run_all.print_summary([good, bad]), 1)

    def test_check_list_has_all_eight_examples_and_the_unit_tests(self) -> None:
        names = [name for name, _ in run_all.build_checks()]
        self.assertEqual(sum(name.startswith("Example:") for name in names), 8)
        self.assertIn("Unit tests (all)", names)


if __name__ == "__main__":
    unittest.main()
