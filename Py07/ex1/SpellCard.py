from ex0.Card import Card

class SpellCard(Card):
    def __init__(self, name: str = None, cost: int = None,
                 rarity: str = None, effect_type: str = None):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        return (self.resolve_effect(["common"]))

    def resolve_effect(self, targets: list) -> dict:
        return (
            {
                'card_played': self.name,
                'mana_used': self.cost,
                'effect': self.effect_type
            }
        )