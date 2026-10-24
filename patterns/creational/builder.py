"""Builder pattern (Creational).

Idea: build a complex object step by step. Optional parts are added only
when needed, and the final object is created by build().

Run this file on its own:  python -m patterns.creational.builder
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

VALID_SIZES = ("small", "medium", "large")
VALID_CRUSTS = ("regular", "thin", "cheese-burst")


@dataclass(frozen=True)
class Pizza:
    """The final product. 'frozen' means it cannot be changed after creation."""

    size: str
    crust: str
    toppings: tuple[str, ...]
    extra_cheese: bool

    def describe(self) -> str:
        toppings_text = ", ".join(self.toppings) if self.toppings else "none"
        cheese_text = "yes" if self.extra_cheese else "no"
        return (
            f"{self.size} pizza, {self.crust} crust, "
            f"toppings: {toppings_text}, extra cheese: {cheese_text}"
        )


class PizzaBuilder:
    """Collects the choices, then creates a Pizza in build()."""

    def __init__(self) -> None:
        self._size: Optional[str] = None
        self._crust: str = "regular"  # default value
        self._toppings: list[str] = []
        self._extra_cheese: bool = False

    def set_size(self, size: str) -> PizzaBuilder:
        if size not in VALID_SIZES:
            raise ValueError(f"Size must be one of {VALID_SIZES}.")
        self._size = size
        return self  # returning self lets us chain calls

    def set_crust(self, crust: str) -> PizzaBuilder:
        if crust not in VALID_CRUSTS:
            raise ValueError(f"Crust must be one of {VALID_CRUSTS}.")
        self._crust = crust
        return self

    def add_topping(self, topping: str) -> PizzaBuilder:
        if not topping.strip():
            raise ValueError("Topping name cannot be empty.")
        self._toppings.append(topping.strip())
        return self

    def add_extra_cheese(self) -> PizzaBuilder:
        self._extra_cheese = True
        return self

    def build(self) -> Pizza:
        if self._size is None:
            raise ValueError("Pizza size is required before build().")
        return Pizza(
            size=self._size,
            crust=self._crust,
            toppings=tuple(self._toppings),  # copy, so later changes do not leak
            extra_cheese=self._extra_cheese,
        )


def demo() -> None:
    plain = PizzaBuilder().set_size("small").build()
    loaded = (
        PizzaBuilder()
        .set_size("large")
        .set_crust("thin")
        .add_topping("onion")
        .add_topping("olives")
        .add_extra_cheese()
        .build()
    )
    print(plain.describe())
    print(loaded.describe())


if __name__ == "__main__":
    demo()
