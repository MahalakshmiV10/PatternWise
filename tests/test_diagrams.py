"""Compares each Mermaid diagram with the real Python classes and methods.

It checks names only. It cannot check that Mermaid draws the diagram correctly.
"""
import importlib
import inspect
import re
import unittest
from pathlib import Path

DIAGRAM_FOLDER = Path(__file__).resolve().parent.parent / "diagrams"

DIAGRAMS = {
    "singleton.mmd": "patterns.creational.singleton",
    "factory_method.mmd": "patterns.creational.factory_method",
    "builder.mmd": "patterns.creational.builder",
    "adapter.mmd": "patterns.structural.adapter",
    "decorator.mmd": "patterns.structural.decorator",
    "facade.mmd": "patterns.structural.facade",
    "strategy.mmd": "patterns.behavioural.strategy",
    "observer.mmd": "patterns.behavioural.observer",
}


def parse_diagram(text: str) -> dict[str, set[str]]:
    """Return {class_name: {method_names}} found in a Mermaid class diagram."""
    classes: dict[str, set[str]] = {}
    current = None
    for line in text.splitlines():
        stripped = line.strip()
        opening = re.match(r"class\s+(\w+)\s*\{", stripped)
        plain = re.match(r"class\s+(\w+)\s*$", stripped)
        if opening:
            current = opening.group(1)
            classes[current] = set()
        elif plain:
            classes[plain.group(1)] = set()
        elif stripped == "}":
            current = None
        elif current and "(" in stripped:
            method = re.search(r"(\w+)\(", stripped)
            if method:
                classes[current].add(method.group(1))
    return classes


class TestDiagramsMatchCode(unittest.TestCase):
    def test_every_pattern_has_a_diagram(self) -> None:
        for filename in DIAGRAMS:
            self.assertTrue((DIAGRAM_FOLDER / filename).exists(), filename)

    def test_diagrams_start_with_class_diagram_keyword(self) -> None:
        for filename in DIAGRAMS:
            first_line = (DIAGRAM_FOLDER / filename).read_text(encoding="utf-8").splitlines()[0]
            self.assertEqual(first_line.strip(), "classDiagram", filename)

    def test_diagram_classes_and_methods_exist_in_code(self) -> None:
        for filename, module_name in DIAGRAMS.items():
            module = importlib.import_module(module_name)
            parsed = parse_diagram((DIAGRAM_FOLDER / filename).read_text(encoding="utf-8"))
            for class_name, methods in parsed.items():
                with self.subTest(diagram=filename, cls=class_name):
                    self.assertTrue(hasattr(module, class_name), f"{class_name} not in code")
                    for method in methods:
                        self.assertTrue(
                            hasattr(getattr(module, class_name), method),
                            f"{class_name}.{method} not in code",
                        )

    def test_every_code_class_is_in_the_diagram(self) -> None:
        for filename, module_name in DIAGRAMS.items():
            module = importlib.import_module(module_name)
            parsed = parse_diagram((DIAGRAM_FOLDER / filename).read_text(encoding="utf-8"))
            defined_here = {
                name
                for name, cls in inspect.getmembers(module, inspect.isclass)
                if cls.__module__ == module.__name__
            }
            with self.subTest(diagram=filename):
                self.assertEqual(defined_here, set(parsed))

    def test_public_methods_in_code_are_listed_in_diagram(self) -> None:
        """Catches methods that exist in the code but are missing from the diagram."""
        for filename, module_name in DIAGRAMS.items():
            module = importlib.import_module(module_name)
            parsed = parse_diagram((DIAGRAM_FOLDER / filename).read_text(encoding="utf-8"))
            for class_name, listed in parsed.items():
                cls = getattr(module, class_name)
                own_public = {
                    name
                    for name, member in vars(cls).items()
                    if not name.startswith("_")
                    and (inspect.isfunction(member) or isinstance(member, (classmethod, staticmethod)))
                }
                with self.subTest(diagram=filename, cls=class_name):
                    self.assertTrue(own_public <= listed, f"missing in diagram: {own_public - listed}")


if __name__ == "__main__":
    unittest.main()
