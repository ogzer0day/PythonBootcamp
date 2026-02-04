from abc import ABC, abstractmethod


class Combatable(ABC):
    """Interface for combat-capable objects."""

    @abstractmethod
    def attack(self, target) -> dict:
        """Perform an attack on a target."""
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        """Defend against incoming damage."""
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        """Return combat-related stats."""
        pass
