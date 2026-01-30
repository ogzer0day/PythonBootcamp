from ex0.Card import Card
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex0.CreatureCard import CreatureCard

import random

class Deck():
    def __init__(self):
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return (True)
        return (False)

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        return self.cards.pop()

    def get_deck_stats(self) -> dict:
        total_cards = len(self.cards)
        creatures = sum([1 for card in self.cards if isinstance(card, SpellCard)])
        spells = sum([1 for card in self.cards if  isinstance(card, ArtifactCard)])
        artifacts = sum([1 for card in self.cards if  isinstance(card, CreatureCard)])
        avg_cost = (sum(card.cost for card in self.cards) / total_cards if total_cards else 0)
        return (
            {
                "total_cards": total_cards,
                "creatures": creatures,
                "spells": spells,
                "artifacts": artifacts,
                "avg_cost": f"{avg_cost:.1f}"
            }
            )