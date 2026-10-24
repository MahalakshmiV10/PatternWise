"""Facade pattern (Structural).

Idea: give one simple class that hides a group of complicated classes
(the subsystem). The client calls one method instead of many.

Run this file on its own:  python -m patterns.structural.facade
"""
from typing import Optional


class Amplifier:
    def turn_on(self) -> str:
        return "Amplifier: power on"

    def set_volume(self, level: int) -> str:
        if not 0 <= level <= 10:
            raise ValueError("Volume must be between 0 and 10.")
        return f"Amplifier: volume set to {level}"

    def turn_off(self) -> str:
        return "Amplifier: power off"


class Projector:
    def turn_on(self) -> str:
        return "Projector: power on"

    def turn_off(self) -> str:
        return "Projector: power off"


class StreamingPlayer:
    def play(self, title: str) -> str:
        return f"Player: playing '{title}'"

    def stop(self) -> str:
        return "Player: stopped"


class HomeTheaterFacade:
    """Simple front door to the amplifier, projector and player."""

    def __init__(
        self,
        amplifier: Optional[Amplifier] = None,
        projector: Optional[Projector] = None,
        player: Optional[StreamingPlayer] = None,
    ) -> None:
        # Defaults are created here; tests can pass in their own objects.
        self._amplifier = amplifier or Amplifier()
        self._projector = projector or Projector()
        self._player = player or StreamingPlayer()
        self._is_playing = False

    def watch_movie(self, title: str) -> list[str]:
        """Start everything in the correct order with ONE call."""
        if not title.strip():
            raise ValueError("Movie title cannot be empty.")
        steps = [
            self._projector.turn_on(),
            self._amplifier.turn_on(),
            self._amplifier.set_volume(5),
            self._player.play(title),
        ]
        self._is_playing = True
        return steps

    def end_movie(self) -> list[str]:
        """Shut everything down in the correct order with ONE call."""
        if not self._is_playing:
            raise RuntimeError("No movie is playing.")
        steps = [
            self._player.stop(),
            self._amplifier.turn_off(),
            self._projector.turn_off(),
        ]
        self._is_playing = False
        return steps


def demo() -> None:
    theater = HomeTheaterFacade()
    for line in theater.watch_movie("Inception"):
        print(line)
    print("---")
    for line in theater.end_movie():
        print(line)


if __name__ == "__main__":
    demo()
