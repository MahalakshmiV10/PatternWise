"""Strategy pattern (Behavioural).

Idea: put each algorithm in its own class with the same interface, so the
algorithm can be swapped at run time.

Run this file on its own:  python -m patterns.behavioural.strategy
"""
import math
from abc import ABC, abstractmethod


class ShippingStrategy(ABC):
    """Common interface for all shipping-cost algorithms."""

    @abstractmethod
    def calculate_cost(self, weight_kg: float) -> int:
        """Return the shipping cost in rupees."""


class StandardShipping(ShippingStrategy):
    def calculate_cost(self, weight_kg: float) -> int:
        return 40 + 10 * math.ceil(weight_kg)


class ExpressShipping(ShippingStrategy):
    def calculate_cost(self, weight_kg: float) -> int:
        return 100 + 25 * math.ceil(weight_kg)


class FreeShipping(ShippingStrategy):
    def calculate_cost(self, weight_kg: float) -> int:
        return 0


class Order:
    """Context: uses a strategy but does not know which one it is."""

    def __init__(self, weight_kg: float, strategy: ShippingStrategy) -> None:
        if weight_kg <= 0:
            raise ValueError("Weight must be greater than zero.")
        self._weight_kg = weight_kg
        self.set_strategy(strategy)

    def set_strategy(self, strategy: ShippingStrategy) -> None:
        if not isinstance(strategy, ShippingStrategy):
            raise TypeError("Strategy must be a ShippingStrategy.")
        self._strategy = strategy

    def shipping_cost(self) -> int:
        return self._strategy.calculate_cost(self._weight_kg)


def demo() -> None:
    order = Order(2.5, StandardShipping())
    print("Standard shipping: Rs", order.shipping_cost())
    order.set_strategy(ExpressShipping())  # swap at run time
    print("Express shipping:  Rs", order.shipping_cost())
    order.set_strategy(FreeShipping())
    print("Free shipping:     Rs", order.shipping_cost())


if __name__ == "__main__":
    demo()
