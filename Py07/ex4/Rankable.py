from abc import ABC, abstractmethod


class Rankable(ABC):
    """Interface for objects that can be ranked or rated."""

    @abstractmethod
    def calculate_rating(self) -> int:
        """Calculate and return the current rating."""
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """Update the object with additional wins."""
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """Update the object with additional losses."""
        pass

    @abstractmethod
    def get_rank_info(self) -> dict:
        """Return ranking-related information."""
        pass
