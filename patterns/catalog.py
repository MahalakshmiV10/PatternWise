"""Information about the eight patterns, used by the menu in main.py and run_all.py."""
from dataclasses import dataclass
from typing import Optional

CATEGORIES = ("Creational", "Structural", "Behavioural")


@dataclass(frozen=True)
class PatternInfo:
    number: int
    name: str
    category: str
    module: str  # dotted module path that has a demo() function
    purpose: str
    analogy: str
    use_case: str


PATTERNS: tuple[PatternInfo, ...] = (
    PatternInfo(
        1, "Singleton", "Creational", "patterns.creational.singleton",
        "Make sure a class has only one object and give everyone access to it.",
        "A school has one principal's office. Everyone who needs the principal goes to the same place.",
        "Application settings shared by the whole program.",
    ),
    PatternInfo(
        2, "Factory Method", "Creational", "patterns.creational.factory_method",
        "Let subclasses decide which concrete object is created.",
        "A hotel booking desk: you ask for 'a room' and each hotel branch gives its own kind of room.",
        "Sending notifications by Email or by SMS.",
    ),
    PatternInfo(
        3, "Builder", "Creational", "patterns.creational.builder",
        "Build a complex object step by step, with optional parts.",
        "Ordering a custom sandwich: you choose bread, fillings and sauce one step at a time.",
        "Creating a pizza order with optional toppings and extra cheese.",
    ),
    PatternInfo(
        4, "Adapter", "Structural", "patterns.structural.adapter",
        "Make a class with an incompatible interface work with code that expects another interface.",
        "A travel plug adapter that lets an Indian plug fit a foreign socket.",
        "Using an old Fahrenheit sensor in an app that expects Celsius.",
    ),
    PatternInfo(
        5, "Decorator", "Structural", "patterns.structural.decorator",
        "Add behaviour to an object by wrapping it, without creating many subclasses.",
        "Adding toppings to an ice cream: each topping wraps the previous one and adds to the price.",
        "A coffee order with optional milk and sugar.",
    ),
    PatternInfo(
        6, "Facade", "Structural", "patterns.structural.facade",
        "Provide one simple interface to a group of complicated classes.",
        "The 'Movie mode' button on a smart remote that switches on many devices at once.",
        "Starting and stopping a home theater with one method call.",
    ),
    PatternInfo(
        7, "Strategy", "Behavioural", "patterns.behavioural.strategy",
        "Keep each algorithm in its own class so it can be swapped at run time.",
        "Going to college by bus, bike or car: same goal, different method.",
        "Calculating shipping cost with Standard, Express or Free shipping.",
    ),
    PatternInfo(
        8, "Observer", "Behavioural", "patterns.behavioural.observer",
        "Notify many objects automatically when one object publishes something.",
        "Subscribers of a YouTube channel get notified when a new video is uploaded.",
        "A news publisher sending messages to subscribers.",
    ),
)


def get_pattern(number: int) -> Optional[PatternInfo]:
    """Return the pattern with this number, or None if it does not exist."""
    for info in PATTERNS:
        if info.number == number:
            return info
    return None


def patterns_by_category() -> dict[str, list[PatternInfo]]:
    """Group the patterns by category, keeping the standard category order."""
    grouped: dict[str, list[PatternInfo]] = {name: [] for name in CATEGORIES}
    for info in PATTERNS:
        grouped[info.category].append(info)
    return grouped
