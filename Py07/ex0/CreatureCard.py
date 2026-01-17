from Card import Card


class CreatureCard(Card):

    def __init__(self, name: str, cost: int, rarity: str,
                 type: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health
        self.type = type

    def play(self, game_state: dict) -> dict:
        return (game_state)

    def attack_target(self, target) -> dict:
        return (target)
