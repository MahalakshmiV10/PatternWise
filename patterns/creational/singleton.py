"""Singleton pattern (Creational).

Idea: a class that can have only ONE object. Every time you ask for it,
you get the same object back.

Run this file on its own:  python -m patterns.creational.singleton
"""
from __future__ import annotations

from typing import Any, Optional


class AppConfig:
    """Application settings shared by the whole program."""

    # The one and only instance is stored on the class itself.
    _instance: Optional["AppConfig"] = None
    _settings: dict[str, Any]

    def __new__(cls) -> "AppConfig":
        # __new__ creates the object. We create it only the first time.
        if cls._instance is None:
            instance = super().__new__(cls)
            instance._settings = {}
            cls._instance = instance
        return cls._instance

    def set_setting(self, key: str, value: Any) -> None:
        """Save a setting. The name cannot be empty."""
        if not key:
            raise ValueError("Setting name cannot be empty.")
        self._settings[key] = value

    def get_setting(self, key: str, default: Any = None) -> Any:
        """Read a setting, or return `default` if it does not exist."""
        return self._settings.get(key, default)

    def clear_settings(self) -> None:
        """Remove all settings."""
        self._settings.clear()

    @classmethod
    def reset_instance(cls) -> None:
        """Forget the shared object. Used by tests so they do not affect each other."""
        cls._instance = None


def demo() -> None:
    first = AppConfig()
    second = AppConfig()
    first.set_setting("theme", "dark")

    print("Same object?", first is second)
    print("Theme read through 'second':", second.get_setting("theme"))

    AppConfig.reset_instance()  # clean up so the demo can be repeated


if __name__ == "__main__":
    demo()
