import unittest

from patterns.behavioural.observer import NewsPublisher, Observer, Subscriber


class TestObserver(unittest.TestCase):
    def setUp(self) -> None:
        self.publisher = NewsPublisher()
        self.asha = Subscriber("Asha")
        self.ravi = Subscriber("Ravi")

    def test_all_subscribers_are_notified(self) -> None:
        self.publisher.attach(self.asha)
        self.publisher.attach(self.ravi)
        count = self.publisher.publish("News 1")
        self.assertEqual(count, 2)
        self.assertEqual(self.asha.received_messages, ["News 1"])
        self.assertEqual(self.ravi.received_messages, ["News 1"])

    def test_detached_observer_stops_receiving(self) -> None:
        self.publisher.attach(self.asha)
        self.publisher.attach(self.ravi)
        self.publisher.publish("News 1")
        self.publisher.detach(self.ravi)
        count = self.publisher.publish("News 2")
        self.assertEqual(count, 1)
        self.assertEqual(self.asha.received_messages, ["News 1", "News 2"])
        self.assertEqual(self.ravi.received_messages, ["News 1"])

    def test_publish_with_no_subscribers(self) -> None:
        self.assertEqual(self.publisher.publish("Nobody listens"), 0)

    def test_duplicate_attach_is_ignored(self) -> None:
        self.publisher.attach(self.asha)
        self.publisher.attach(self.asha)
        self.publisher.publish("Once")
        self.assertEqual(self.asha.received_messages, ["Once"])

    def test_detach_unknown_observer_fails(self) -> None:
        with self.assertRaises(ValueError):
            self.publisher.detach(self.asha)

    def test_empty_message_is_rejected(self) -> None:
        self.publisher.attach(self.asha)
        with self.assertRaises(ValueError):
            self.publisher.publish("  ")
        self.assertEqual(self.asha.received_messages, [])

    def test_non_observer_is_rejected(self) -> None:
        with self.assertRaises(TypeError):
            self.publisher.attach("not an observer")  # type: ignore[arg-type]

    def test_messages_arrive_in_order(self) -> None:
        self.publisher.attach(self.asha)
        for text in ("one", "two", "three"):
            self.publisher.publish(text)
        self.assertEqual(self.asha.received_messages, ["one", "two", "three"])

    def test_observer_interface_is_abstract(self) -> None:
        with self.assertRaises(TypeError):
            Observer()  # type: ignore[abstract]


if __name__ == "__main__":
    unittest.main()
