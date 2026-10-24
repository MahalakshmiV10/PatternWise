import unittest

from patterns.structural.facade import (
    Amplifier,
    HomeTheaterFacade,
    Projector,
    StreamingPlayer,
)


class RecordingAmplifier(Amplifier):
    """Test helper: records the order of calls in a shared list."""

    def __init__(self, log: list[str]) -> None:
        self.log = log

    def turn_on(self) -> str:
        self.log.append("amp_on")
        return super().turn_on()

    def turn_off(self) -> str:
        self.log.append("amp_off")
        return super().turn_off()


class RecordingProjector(Projector):
    def __init__(self, log: list[str]) -> None:
        self.log = log

    def turn_on(self) -> str:
        self.log.append("projector_on")
        return super().turn_on()

    def turn_off(self) -> str:
        self.log.append("projector_off")
        return super().turn_off()


class RecordingPlayer(StreamingPlayer):
    def __init__(self, log: list[str]) -> None:
        self.log = log

    def play(self, title: str) -> str:
        self.log.append(f"play:{title}")
        return super().play(title)

    def stop(self) -> str:
        self.log.append("stop")
        return super().stop()


class TestFacade(unittest.TestCase):
    def setUp(self) -> None:
        self.log: list[str] = []
        self.theater = HomeTheaterFacade(
            RecordingAmplifier(self.log),
            RecordingProjector(self.log),
            RecordingPlayer(self.log),
        )

    def test_watch_movie_coordinates_subsystems_in_order(self) -> None:
        self.theater.watch_movie("Dune")
        self.assertEqual(self.log, ["projector_on", "amp_on", "play:Dune"])

    def test_watch_movie_returns_step_messages(self) -> None:
        steps = self.theater.watch_movie("Dune")
        self.assertEqual(len(steps), 4)
        self.assertIn("volume set to 5", steps[2])
        self.assertIn("Dune", steps[3])

    def test_end_movie_shuts_down_in_order(self) -> None:
        self.theater.watch_movie("Dune")
        self.log.clear()
        self.theater.end_movie()
        self.assertEqual(self.log, ["stop", "amp_off", "projector_off"])

    def test_end_movie_without_watching_fails(self) -> None:
        with self.assertRaises(RuntimeError):
            self.theater.end_movie()

    def test_end_movie_twice_fails(self) -> None:
        self.theater.watch_movie("Dune")
        self.theater.end_movie()
        with self.assertRaises(RuntimeError):
            self.theater.end_movie()

    def test_empty_title_is_rejected_and_nothing_starts(self) -> None:
        with self.assertRaises(ValueError):
            self.theater.watch_movie("  ")
        self.assertEqual(self.log, [])

    def test_default_subsystems_work(self) -> None:
        theater = HomeTheaterFacade()
        self.assertEqual(len(theater.watch_movie("Test")), 4)
        self.assertEqual(len(theater.end_movie()), 3)

    def test_amplifier_volume_limits(self) -> None:
        amplifier = Amplifier()
        with self.assertRaises(ValueError):
            amplifier.set_volume(11)
        with self.assertRaises(ValueError):
            amplifier.set_volume(-1)
        self.assertIn("10", amplifier.set_volume(10))


if __name__ == "__main__":
    unittest.main()
