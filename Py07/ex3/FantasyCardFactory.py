from ex3.CardFactory import CardFactory
from ex0.Card import Card
import random

class FantasyCardFactory(CardFactory):

    def create_creature(self, name_or_power) -> Card:
        creatures = ["Fire Dragon", "Goblin Warrior", "Elf Archer"]

        if isinstance(name_or_power, int):
            name = random.choice(creatures)
            return Card(name, name_or_power)
        return Card(name_or_power, random.randint(2, 5))

    def create_spell(self, name_or_power) -> Card:
        spells = ["Fireball", "Lightning Bolt", "Ice Blast"]

        if isinstance(name_or_power, int):
            name = random.choice(spells)
            return Card(name, name_or_power)
        return Card(name_or_power, random.randint(2, 4))

    def create_artifact(self, name_or_power) -> Card:
        artifacts = ["Mana Ring", "Crystal Staff", "Ancient Amulet"]

        if isinstance(name_or_power, int):
            name = random.choice(artifacts)
            return Card(name, name_or_power)
        return Card(name_or_power, random.randint(1, 3))

    def create_themed_deck(self, size: int) -> dict:
        deck = {"creatures": [], "spells": [], "artifacts": []}

        for _ in range(size):
            choice = random.choice(["creatures", "spells", "artifacts"])

            if choice == "creatures":
                deck["creatures"].append(self.create_creature(random.randint(2, 5)))
            elif choice == "spells":
                deck["spells"].append(self.create_spell(random.randint(1, 4)))
            else:
                deck["artifacts"].append(self.create_artifact(random.randint(1, 3)))

        return deck

    def get_supported_types(self) -> dict:
        return {
            "creatures": ["fire_dragon", "goblin_warrior", "elf_archer"],
            "spells": ["fireball", "lightning_bolt", "ice_blast"],
            "artifacts": ["mana_ring", "crystal_staff", "ancient_amulet"]
        }
