import unittest

from patterns.creational.singleton import AppConfig


class TestSingleton(unittest.TestCase):
    def setUp(self) -> None:
        # The Singleton keeps state between tests, so we reset it every time.
        AppConfig.reset_instance()

    def tearDown(self) -> None:
        AppConfig.reset_instance()

    def test_same_object_is_returned(self) -> None:
        self.assertIs(AppConfig(), AppConfig())

    def test_state_is_shared(self) -> None:
        AppConfig().set_setting("theme", "dark")
        self.assertEqual(AppConfig().get_setting("theme"), "dark")

    def test_missing_setting_returns_default(self) -> None:
        self.assertIsNone(AppConfig().get_setting("missing"))
        self.assertEqual(AppConfig().get_setting("missing", "fallback"), "fallback")

    def test_empty_setting_name_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            AppConfig().set_setting("", "value")

    def test_clear_settings(self) -> None:
        config = AppConfig()
        config.set_setting("a", 1)
        config.clear_settings()
        self.assertIsNone(config.get_setting("a"))

    def test_reset_instance_gives_fresh_object(self) -> None:
        old = AppConfig()
        old.set_setting("a", 1)
        AppConfig.reset_instance()
        new = AppConfig()
        self.assertIsNot(old, new)
        self.assertIsNone(new.get_setting("a"))


if __name__ == "__main__":
    unittest.main()
