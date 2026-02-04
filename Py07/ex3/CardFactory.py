from abc import ABC, abstractmethod
from ex0.Card import Card


class CardFactory(ABC):
    """Abstract factory for creating cards and decks."""

    @abstractmethod
    def create_creature(self, name_or_power) -> Card:
        """Create a creature card."""
        pass

    @abstractmethod
    def create_spell(self, name_or_power) -> Card:
        """Create a spell card."""
        pass

    @abstractmethod
    def create_artifact(self, name_or_power) -> Card:
        """Create an artifact card."""
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        """Create a deck of cards with a specific theme."""
        pass

    @abstractmethod
    def get_supported_types(self) -> dict:
        """Return the types of cards this factory can create."""
        pass
