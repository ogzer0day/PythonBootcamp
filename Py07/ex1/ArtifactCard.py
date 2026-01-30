from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, 
                 effect: str, 
                 rarity: str, 
                 durability: int = 10):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        return (self.activate_ability())

    def activate_ability(self) -> dict:
        return (
            {
                'card_played': self.name,
                'mana_used': self.cost,
                'effect': self.effect
            }
        )