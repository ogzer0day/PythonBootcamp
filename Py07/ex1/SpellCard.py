from ex0.Card import Card


class SpellCard(Card):
    """A spell card that resolves an immediate effect when played."""

    def __init__(
        self,
        name: str = None,
        cost: int = None,
        rarity: str = None,
        effect_type: str = None,
    ):
        """Initialize a spell card with a name,
        cost, rarity, and effect type."""
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        """Play the spell and resolve its effect."""
        return self.resolve_effect(["common"])

    def resolve_effect(self, targets: list) -> dict:
        """Resolve the spell's effect on the given targets."""
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect_type,
        }
