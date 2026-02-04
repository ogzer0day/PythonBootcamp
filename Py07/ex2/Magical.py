from abc import ABC, abstractmethod


class Magical(ABC):
    """Interface for magic-related abilities."""

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Cast a spell on the given targets."""
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        """Channel a specified amount of mana."""
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict:
        """Return magic-related statistics or actions."""
        pass
