"""Decorator pattern (Structural).

Idea: add extra behaviour to an object by wrapping it, instead of creating
many subclasses. Wrappers can be stacked in any order.

Note: this is the design pattern, NOT Python's @decorator syntax.

Run this file on its own:  python -m patterns.structural.decorator
"""
from abc import ABC, abstractmethod


class Beverage(ABC):
    """Common interface for drinks and for wrappers around drinks."""

    @abstractmethod
    def description(self) -> str:
        """Return a text description."""

    @abstractmethod
    def cost(self) -> int:
        """Return the price in rupees."""


class Espresso(Beverage):
    def description(self) -> str:
        return "Espresso"

    def cost(self) -> int:
        return 80


class AddOnDecorator(Beverage, ABC):
    """Base wrapper: it holds another Beverage inside."""

    def __init__(self, beverage: Beverage) -> None:
        if not isinstance(beverage, Beverage):
            raise TypeError("Can only decorate a Beverage.")
        self._beverage = beverage


class MilkDecorator(AddOnDecorator):
    def description(self) -> str:
        return f"{self._beverage.description()} + Milk"

    def cost(self) -> int:
        return self._beverage.cost() + 20


class SugarDecorator(AddOnDecorator):
    def description(self) -> str:
        return f"{self._beverage.description()} + Sugar"

    def cost(self) -> int:
        return self._beverage.cost() + 5


def demo() -> None:
    plain = Espresso()
    sweet_milk_coffee = SugarDecorator(MilkDecorator(Espresso()))
    print(f"{plain.description()}: Rs {plain.cost()}")
    print(f"{sweet_milk_coffee.description()}: Rs {sweet_milk_coffee.cost()}")


if __name__ == "__main__":
    demo()
