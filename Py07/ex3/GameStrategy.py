from abc import ABC, abstractmethod


class GameStrategy(ABC):
    """Abstract base class for game strategies."""

    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """Execute a turn using this strategy."""
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """Return the name of the strategy."""
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        """Determine target priority based on strategy."""
        pass
