from abc import ABC, abstractmethod


class Card(ABC):
    """Base class for all cards."""

    def __init__(self, name: str = None, cost: int = None, rarity: str = None):
        """Initialize a card with name, cost, and rarity."""
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """Play the card and update the game state."""
        pass

    def get_card_info(self) -> dict:
        """Return basic info about the card."""
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": None,
            "attack": None,
            "health": None,
        }

    def is_playable(self, available_mana: int) -> bool:
        """Check if the card can be played with available mana."""
        return available_mana > 3
