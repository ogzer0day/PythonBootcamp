from ex0.Card import Card

class CreatureCard(Card):

    def __init__(self, name: str = None, cost: int = None,
                 effect: str = None, rarity: str = None, type: str = None,
                 attack: int = None, health: int = None):
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health
        self.type = type
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        return (
            {
                "card_player": self.name,
                "mana_used": self.cost,
                "effect": self.effect
            }
        )

    def attack_target(self, target) -> dict:
        return (target)
