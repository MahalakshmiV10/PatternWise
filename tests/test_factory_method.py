import unittest

from patterns.creational.factory_method import (
    EmailNotification,
    EmailService,
    Notification,
    NotificationService,
    SmsNotification,
    SmsService,
)


class TestFactoryMethod(unittest.TestCase):
    def test_email_service_creates_email_notification(self) -> None:
        self.assertIsInstance(EmailService().create_notification(), EmailNotification)

    def test_sms_service_creates_sms_notification(self) -> None:
        self.assertIsInstance(SmsService().create_notification(), SmsNotification)

    def test_notify_uses_the_right_channel(self) -> None:
        self.assertEqual(EmailService().notify("Hi"), "Email sent: Hi")
        self.assertEqual(SmsService().notify("Hi"), "SMS sent: Hi")

    def test_empty_message_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            EmailService().notify("")

    def test_whitespace_message_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            SmsService().notify("   ")

    def test_abstract_classes_cannot_be_created(self) -> None:
        with self.assertRaises(TypeError):
            NotificationService()  # type: ignore[abstract]
        with self.assertRaises(TypeError):
            Notification()  # type: ignore[abstract]

    def test_client_code_works_with_any_service(self) -> None:
        for service in (EmailService(), SmsService()):
            self.assertIn("Hello", service.notify("Hello"))


if __name__ == "__main__":
    unittest.main()
