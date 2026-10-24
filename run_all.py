"""Run every PatternWise check with one command:  python run_all.py

Checks: 8 example programs, the app's --list command, and the whole unittest suite.
Exit code 0 = everything passed, 1 = at least one check failed.
"""
import re
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path

from patterns.catalog import PATTERNS

ROOT = Path(__file__).resolve().parent


@dataclass
class CheckResult:
    name: str
    passed: bool
    seconds: float
    output: str
    detail: str


def run_check(name: str, command: list[str], timeout: int = 120) -> CheckResult:
    """Run one command and report honestly: pass only if exit code is 0."""
    start = time.perf_counter()
    try:
        completed = subprocess.run(
            command,
            cwd=ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout,
        )
    except FileNotFoundError as error:
        return CheckResult(name, False, time.perf_counter() - start, str(error), "command not found")
    except subprocess.TimeoutExpired:
        return CheckResult(name, False, time.perf_counter() - start, "", f"timed out after {timeout}s")

    seconds = time.perf_counter() - start
    output = (completed.stdout or "") + (completed.stderr or "")
    passed = completed.returncode == 0
    detail = f"exit code {completed.returncode}"
    ran = re.search(r"Ran (\d+) tests?", output)
    if ran:
        detail = f"{ran.group(1)} tests, exit code {completed.returncode}"
    return CheckResult(name, passed, seconds, output, detail)


def build_checks() -> list[tuple[str, list[str]]]:
    python = sys.executable
    checks: list[tuple[str, list[str]]] = []
    for info in PATTERNS:
        checks.append((f"Example: {info.name}", [python, "-m", info.module]))
    checks.append(("App: main.py --list", [python, "main.py", "--list"]))
    checks.append((
        "Unit tests (all)",
        [python, "-m", "unittest", "discover", "-s", "tests", "-t", ".", "-v"],
    ))
    return checks


def print_summary(results: list[CheckResult]) -> int:
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    for result in results:
        label = "PASS" if result.passed else "FAIL"
        print(f"[{label}] {result.name:<28} {result.detail} ({result.seconds:.2f}s)")
    failed = [result for result in results if not result.passed]
    print("-" * 60)
    print(f"{len(results) - len(failed)} passed, {len(failed)} failed, {len(results)} total")
    if failed:
        print("RESULT: FAILED")
        return 1
    print("RESULT: ALL CHECKS PASSED")
    return 0


def main() -> int:
    print(f"Python {sys.version.split()[0]} | project folder: {ROOT}")
    results: list[CheckResult] = []
    for name, command in build_checks():
        result = run_check(name, command)
        results.append(result)
        print(f"[{'PASS' if result.passed else 'FAIL'}] {name}")
        if not result.passed:
            print("---- output of failed check ----")
            print(result.output.rstrip())
            print("--------------------------------")
    return print_summary(results)


if __name__ == "__main__":
    raise SystemExit(main())
