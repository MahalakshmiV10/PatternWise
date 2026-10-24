"""Adapter pattern (Structural).

Idea: make an existing class with the WRONG interface work with code that
expects a different interface, without changing the existing class.

Run this file on its own:  python -m patterns.structural.adapter
"""
from abc import ABC, abstractmethod

ABSOLUTE_ZERO_FAHRENHEIT = -459.67


class CelsiusSensor(ABC):
    """Target interface: what our application expects."""

    @abstractmethod
    def get_temperature_celsius(self) -> float:
        """Return the temperature in Celsius."""


class LegacyFahrenheitSensor:
    """Adaptee: old class we cannot (or should not) change."""

    def __init__(self, reading_fahrenheit: float) -> None:
        self._reading_fahrenheit = reading_fahrenheit

    def read_fahrenheit(self) -> float:
        return self._reading_fahrenheit


class FahrenheitToCelsiusAdapter(CelsiusSensor):
    """Adapter: wraps the legacy sensor and speaks the Celsius interface."""

    def __init__(self, legacy_sensor: LegacyFahrenheitSensor) -> None:
        self._legacy_sensor = legacy_sensor

    def get_temperature_celsius(self) -> float:
        fahrenheit = self._legacy_sensor.read_fahrenheit()
        if fahrenheit < ABSOLUTE_ZERO_FAHRENHEIT:
            raise ValueError("Reading is below absolute zero, so it is invalid.")
        return (fahrenheit - 32) * 5 / 9


def show_temperature(sensor: CelsiusSensor) -> str:
    """Client code: it only knows the CelsiusSensor interface."""
    return f"Temperature: {sensor.get_temperature_celsius():.1f} C"


def demo() -> None:
    old_sensor = LegacyFahrenheitSensor(212.0)
    adapter = FahrenheitToCelsiusAdapter(old_sensor)
    print("Legacy reading (F):", old_sensor.read_fahrenheit())
    print(show_temperature(adapter))


if __name__ == "__main__":
    demo()
