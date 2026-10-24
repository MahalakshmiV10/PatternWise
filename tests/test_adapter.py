import unittest

from patterns.structural.adapter import (
    CelsiusSensor,
    FahrenheitToCelsiusAdapter,
    LegacyFahrenheitSensor,
    show_temperature,
)


class TestAdapter(unittest.TestCase):
    def test_boiling_point(self) -> None:
        adapter = FahrenheitToCelsiusAdapter(LegacyFahrenheitSensor(212.0))
        self.assertAlmostEqual(adapter.get_temperature_celsius(), 100.0)

    def test_freezing_point(self) -> None:
        adapter = FahrenheitToCelsiusAdapter(LegacyFahrenheitSensor(32.0))
        self.assertAlmostEqual(adapter.get_temperature_celsius(), 0.0)

    def test_minus_forty_is_the_same_in_both_scales(self) -> None:
        adapter = FahrenheitToCelsiusAdapter(LegacyFahrenheitSensor(-40.0))
        self.assertAlmostEqual(adapter.get_temperature_celsius(), -40.0)

    def test_body_temperature(self) -> None:
        adapter = FahrenheitToCelsiusAdapter(LegacyFahrenheitSensor(98.6))
        self.assertAlmostEqual(adapter.get_temperature_celsius(), 37.0, places=5)

    def test_adapter_matches_target_interface(self) -> None:
        adapter = FahrenheitToCelsiusAdapter(LegacyFahrenheitSensor(50.0))
        self.assertIsInstance(adapter, CelsiusSensor)

    def test_client_code_works_with_adapter(self) -> None:
        adapter = FahrenheitToCelsiusAdapter(LegacyFahrenheitSensor(212.0))
        self.assertEqual(show_temperature(adapter), "Temperature: 100.0 C")

    def test_legacy_sensor_is_unchanged(self) -> None:
        legacy = LegacyFahrenheitSensor(212.0)
        FahrenheitToCelsiusAdapter(legacy).get_temperature_celsius()
        self.assertEqual(legacy.read_fahrenheit(), 212.0)

    def test_reading_below_absolute_zero_is_rejected(self) -> None:
        adapter = FahrenheitToCelsiusAdapter(LegacyFahrenheitSensor(-500.0))
        with self.assertRaises(ValueError):
            adapter.get_temperature_celsius()

    def test_target_interface_is_abstract(self) -> None:
        with self.assertRaises(TypeError):
            CelsiusSensor()  # type: ignore[abstract]


if __name__ == "__main__":
    unittest.main()
