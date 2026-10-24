"""Observer pattern (Behavioural).

Idea: when one object (the subject) changes or publishes something, all
objects that subscribed to it (observers) are told automatically.

Run this file on its own:  python -m patterns.behavioural.observer
"""
from abc import ABC, abstractmethod


class Observer(ABC):
    """Anything that wants to receive notifications."""

    @abstractmethod
    def update(self, message: str) -> None:
        """Called by the publisher when there is news."""


class Subscriber(Observer):
    """A simple observer that remembers every message it receives."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.received_messages: list[str] = []

    def update(self, message: str) -> None:
        self.received_messages.append(message)


class NewsPublisher:
    """Subject: keeps a list of observers and notifies them."""

    def __init__(self) -> None:
        self._observers: list[Observer] = []

    def attach(self, observer: Observer) -> None:
        if not isinstance(observer, Observer):
            raise TypeError("Only Observer objects can subscribe.")
        if observer not in self._observers:  # ignore duplicate subscriptions
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        if observer not in self._observers:
            raise ValueError("This observer is not subscribed.")
        self._observers.remove(observer)

    def publish(self, message: str) -> int:
        """Tell every observer. Returns how many were notified."""
        if not message.strip():
            raise ValueError("Message cannot be empty.")
        for observer in list(self._observers):  # copy: safe if the list changes
            observer.update(message)
        return len(self._observers)


def demo() -> None:
    publisher = NewsPublisher()
    asha = Subscriber("Asha")
    ravi = Subscriber("Ravi")
    publisher.attach(asha)
    publisher.attach(ravi)

    count = publisher.publish("Exam timetable released")
    print(f"First news sent to {count} subscribers")

    publisher.detach(ravi)  # Ravi unsubscribes
    count = publisher.publish("Holiday on Friday")
    print(f"Second news sent to {count} subscriber")

    print("Asha received:", asha.received_messages)
    print("Ravi received:", ravi.received_messages)


if __name__ == "__main__":
    demo()
