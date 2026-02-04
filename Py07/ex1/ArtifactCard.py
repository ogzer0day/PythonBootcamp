from ex0.Card import Card


class ArtifactCard(Card):
    """An artifact card with durability and a special ability."""

    def __init__(
        self,
        name: str = None,
        cost: int = None,
        effect: str = None,
        rarity: str = None,
        durability: int = None,
    ):
        """Initialize an artifact card with effect and durability."""
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        """Play the artifact and activate its ability."""
        return self.activate_ability()

    def activate_ability(self) -> dict:
        """Activate the artifact's special ability."""
        return {"card_played": self.name, "mana_used": self.cost,
                "effect": self.effect}
