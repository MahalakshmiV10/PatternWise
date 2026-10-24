import dataclasses
import unittest

from patterns.creational.builder import Pizza, PizzaBuilder


class TestBuilder(unittest.TestCase):
    def test_minimal_pizza_uses_defaults(self) -> None:
        pizza = PizzaBuilder().set_size("small").build()
        self.assertEqual(pizza.size, "small")
        self.assertEqual(pizza.crust, "regular")
        self.assertEqual(pizza.toppings, ())
        self.assertFalse(pizza.extra_cheese)

    def test_full_configuration(self) -> None:
        pizza = (
            PizzaBuilder()
            .set_size("large")
            .set_crust("thin")
            .add_topping("onion")
            .add_topping("olives")
            .add_extra_cheese()
            .build()
        )
        self.assertEqual(pizza.toppings, ("onion", "olives"))
        self.assertEqual(pizza.crust, "thin")
        self.assertTrue(pizza.extra_cheese)

    def test_builder_methods_return_the_builder(self) -> None:
        builder = PizzaBuilder()
        self.assertIs(builder.set_size("medium"), builder)

    def test_build_without_size_fails(self) -> None:
        with self.assertRaises(ValueError):
            PizzaBuilder().build()

    def test_invalid_size_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            PizzaBuilder().set_size("giant")

    def test_invalid_crust_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            PizzaBuilder().set_crust("stuffed")

    def test_empty_topping_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            PizzaBuilder().add_topping("  ")

    def test_built_pizza_is_not_changed_by_later_builder_calls(self) -> None:
        builder = PizzaBuilder().set_size("small").add_topping("onion")
        first = builder.build()
        builder.add_topping("corn")
        self.assertEqual(first.toppings, ("onion",))

    def test_pizza_cannot_be_modified(self) -> None:
        pizza = PizzaBuilder().set_size("small").build()
        with self.assertRaises(dataclasses.FrozenInstanceError):
            pizza.size = "large"  # type: ignore[misc]

    def test_describe_text(self) -> None:
        pizza = Pizza("small", "regular", (), False)
        self.assertEqual(
            pizza.describe(),
            "small pizza, regular crust, toppings: none, extra cheese: no",
        )


if __name__ == "__main__":
    unittest.main()
