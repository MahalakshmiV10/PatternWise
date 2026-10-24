"""Factory Method pattern (Creational).

Idea: the main code asks a "creator" for an object. Each creator subclass
decides WHICH concrete class to create.

Run this file on its own:  python -m patterns.creational.factory_method
"""
from abc import ABC, abstractmethod


class Notification(ABC):
    """Product interface: everything that can send a message."""

    @abstractmethod
    def send(self, message: str) -> str:
        """Send the message and return a short result text."""


class EmailNotification(Notification):
    def send(self, message: str) -> str:
        return f"Email sent: {message}"


class SmsNotification(Notification):
    def send(self, message: str) -> str:
        return f"SMS sent: {message}"


class NotificationService(ABC):
    """Creator: has the factory method create_notification()."""

    @abstractmethod
    def create_notification(self) -> Notification:
        """The factory method. Subclasses decide the concrete class."""

    def notify(self, message: str) -> str:
        """Common logic that works with ANY notification type."""
        if not message.strip():
            raise ValueError("Message cannot be empty.")
        notification = self.create_notification()
        return notification.send(message)


class EmailService(NotificationService):
    def create_notification(self) -> Notification:
        return EmailNotification()


class SmsService(NotificationService):
    def create_notification(self) -> Notification:
        return SmsNotification()


def demo() -> None:
    for service in (EmailService(), SmsService()):
        print(service.notify("Your exam hall ticket is ready"))


if __name__ == "__main__":
    demo()
