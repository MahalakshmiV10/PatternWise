import unittest

from patterns.structural.decorator import (
    AddOnDecorator,
    Beverage,
    Espresso,
    MilkDecorator,
    SugarDecorator,
)


class TestDecorator(unittest.TestCase):
    def test_plain_espresso(self) -> None:
        drink = Espresso()
        self.assertEqual(drink.description(), "Espresso")
        self.assertEqual(drink.cost(), 80)

    def test_milk_adds_behaviour_and_keeps_original(self) -> None:
        drink = MilkDecorator(Espresso())
        self.assertEqual(drink.description(), "Espresso + Milk")
        self.assertEqual(drink.cost(), 100)

    def test_decorators_can_be_stacked(self) -> None:
        drink = SugarDecorator(MilkDecorator(Espresso()))
        self.assertEqual(drink.description(), "Espresso + Milk + Sugar")
        self.assertEqual(drink.cost(), 105)

    def test_same_decorator_twice(self) -> None:
        drink = MilkDecorator(MilkDecorator(Espresso()))
        self.assertEqual(drink.cost(), 120)
        self.assertEqual(drink.description(), "Espresso + Milk + Milk")

    def test_order_changes_text_but_not_price(self) -> None:
        a = SugarDecorator(MilkDecorator(Espresso()))
        b = MilkDecorator(SugarDecorator(Espresso()))
        self.assertEqual(a.cost(), b.cost())
        self.assertNotEqual(a.description(), b.description())

    def test_wrapped_object_is_not_changed(self) -> None:
        espresso = Espresso()
        MilkDecorator(espresso)
        self.assertEqual(espresso.cost(), 80)

    def test_decorated_drink_is_still_a_beverage(self) -> None:
        self.assertIsInstance(MilkDecorator(Espresso()), Beverage)

    def test_non_beverage_is_rejected(self) -> None:
        with self.assertRaises(TypeError):
            MilkDecorator("not a drink")  # type: ignore[arg-type]

    def test_base_decorator_is_abstract(self) -> None:
        with self.assertRaises(TypeError):
            AddOnDecorator(Espresso())  # type: ignore[abstract]


if __name__ == "__main__":
    unittest.main()
