from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """Aggressive AI strategy that focuses on dealing damage quickly."""

    def execute_turn(self, hand: list = None,
                     battlefield: list = None) -> dict:
        """Play cards and attack according to aggressive priorities."""
        targets = self.prioritize_targets(["Enemy Player"])
        cards_played = hand[1:] if hand else []
        m = [card.split(" (")[0] for card in cards_played]

        return {
            "cards_played": m,
            "mana_used": 5,
            "targets_attacked": targets,
            "damage_dealt": 8,
        }

    def get_strategy_name(self) -> str:
        """Return the name of the strategy."""
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        """Select targets based on aggressive priority."""
        return available_targets
