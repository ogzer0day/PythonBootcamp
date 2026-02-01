from ex3.CardFactory import CardFactory
from ex0.Card import Card
import random
class FantasyCardFactory(CardFactory, Card):
    def create_creature(self, name_or_power) -> Card:
        creatures = [
            ("Fire Dragon", 5),
            ("Goblin Warrior", 2),
            ("Elf Archer", 3)
        ]

        if isinstance(name_or_power, int):
            name, power = random.choice(creatures)
            return Card(name, name_or_power)
        else:
            return Card(name_or_power, random.randint(2, 5))
    
    def create_spell(self, name_or_power) -> Card:
        spells = [
            ("Fireball", 4),
            ("Lightning Bolt", 3),
            ("Ice Blast", 2)
        ]
        if isinstance(name_or_power, int):
            name, _ = random.choice(spells)
            return Card(name, name_or_power)
        else:
            return Card(name, random.randint(2, 4))
    
    def create_artifact(self, name_or_power) -> Card:
        artifacts = [
            ("mana_ring", 1),
            ("Crystal Staff", 2),
            ("Ancient Amulet", 3)
        ]
        if isinstance(name_or_power, int):
            name, _ = random.choice(artifacts)
            return Card(name, name_or_power)
        else:
            return Card(name_or_power, random.randint(1, 3))
    
    def create_themed_deck(self, size: int) -> dict:
        themed_deck = {
            "creatures": [],
            "spells": [],
            "artifacts": []
        }
        for _ in range(size):
            chois = random.choice("creatures", "spells", "artifacts")

            if chois == "creatures":
                themed_deck["creatures"].append(
                    self.create_creature(random.randint(2, 5))
                    )

            elif chois == "spells":
                themed_deck["spells"].append(
                    self.create_spell(random.randint(1, 3)))

            elif chois == "artifacts":
                themed_deck["artifacts"].append(
                    self.create_artifact(random.randint(2, 4)))

        return (themed_deck)
    
    def get_supported_types(self) -> dict:
        return {
            "creatures": ["fire_dragon", "goblin_warrior", "elf_archer"],
            "spells": ["fireball", "lightning_bolt", "ice_blast"],
            "artifacts": ["mana_ring", "crystal_staff", "ancient_amulet"]
        }
