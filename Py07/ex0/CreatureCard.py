from ex0.Card import Card


class CreatureCard(Card):
    """A creature card with attack, health, and optional effects."""

    def __init__(
        self,
        name: str = None,
        cost: int = None,
        effect: str = None,
        rarity: str = None,
        type: str = None,
        attack: int = None,
        health: int = None,
    ):
        """Initialize a creature card with stats and effect."""
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health
        self.type = type
        self.effect = effect

    def play(self, game_state: dict = None) -> dict:
        """Play the creature and apply its effect."""
        return {"card_player": self.name,
                "mana_used": self.cost, "effect": self.effect}

    def attack_target(self, target) -> dict:
        """Attack a target using the creature's attack value."""
        return {"attacker": self.name, "target": target, "damage": self.attack}
