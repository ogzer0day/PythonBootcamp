from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    """A powerful card that supports combat and magic actions."""

    def play(self, game_state: dict) -> dict:
        """Play the card without modifying the game state."""
        return game_state

    def attack(self, target) -> dict:
        """Attack a target with a melee strike."""
        return {
            "attacker": "Arcane Warrior",
            "target": target,
            "damage": 5,
            "combat_type": "melee",
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Cast a spell on the given targets."""
        return {
            "caster": "Arcane Warrior",
            "spell": spell_name,
            "targets": targets,
            "mana_used": 4,
        }

    def defend(self, incoming_damage: int) -> dict:
        """Defend against incoming damage."""
        return {
            "defender": "Arcane Warrior",
            "damage_taken": incoming_damage,
            "damage_blocked": 3,
            "still_alive": True,
        }

    def get_combat_stats(self) -> dict:
        """Return example combat results."""
        return {"Attack result": self.attack("Enemy"),
                "Defense result": self.defend(2)}

    def channel_mana(self, amount: int) -> dict:
        """Channel mana for spell usage."""
        return {"channeled": 3, "total_mana": amount}

    def get_magic_stats(self) -> dict:
        """Return example magic-related actions."""
        return {
            "Spell cast": self.cast_spell("Fireball", ["Enemy1", "Enemy2"]),
            "Mana channel": self.channel_mana(7),
        }
