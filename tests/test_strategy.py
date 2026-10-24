import unittest

from patterns.behavioural.strategy import (
    ExpressShipping,
    FreeShipping,
    Order,
    ShippingStrategy,
    StandardShipping,
)


class TestStrategy(unittest.TestCase):
    def test_standard_cost(self) -> None:
        self.assertEqual(Order(2.5, StandardShipping()).shipping_cost(), 70)

    def test_express_cost(self) -> None:
        self.assertEqual(Order(2.5, ExpressShipping()).shipping_cost(), 175)

    def test_free_cost(self) -> None:
        self.assertEqual(Order(2.5, FreeShipping()).shipping_cost(), 0)

    def test_different_strategies_give_different_results(self) -> None:
        costs = {
            Order(1, strategy).shipping_cost()
            for strategy in (StandardShipping(), ExpressShipping(), FreeShipping())
        }
        self.assertEqual(len(costs), 3)

    def test_strategy_can_be_swapped_at_run_time(self) -> None:
        order = Order(2.5, StandardShipping())
        self.assertEqual(order.shipping_cost(), 70)
        order.set_strategy(ExpressShipping())
        self.assertEqual(order.shipping_cost(), 175)

    def test_partial_kilogram_is_rounded_up(self) -> None:
        self.assertEqual(Order(0.1, StandardShipping()).shipping_cost(), 50)
        self.assertEqual(Order(1, StandardShipping()).shipping_cost(), 50)
        self.assertEqual(Order(1.01, StandardShipping()).shipping_cost(), 60)

    def test_zero_or_negative_weight_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            Order(0, StandardShipping())
        with self.assertRaises(ValueError):
            Order(-3, StandardShipping())

    def test_invalid_strategy_is_rejected(self) -> None:
        with self.assertRaises(TypeError):
            Order(1, "fast")  # type: ignore[arg-type]
        order = Order(1, StandardShipping())
        with self.assertRaises(TypeError):
            order.set_strategy(None)  # type: ignore[arg-type]

    def test_strategy_interface_is_abstract(self) -> None:
        with self.assertRaises(TypeError):
            ShippingStrategy()  # type: ignore[abstract]


if __name__ == "__main__":
    unittest.main()
