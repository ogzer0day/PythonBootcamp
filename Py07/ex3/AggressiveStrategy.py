from ex3.GameStrategy import GameStrategy

class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        targets = self.prioritize_targets(["Enemy Player"])
        return (
            {
                'cards_played': hand[1:],
                'mana_used': 5,
                'targets_attacked': targets,
                'damage_dealt': 8
            }
        )

    def get_strategy_name(self) -> str:
        return ("AggressiveStrategy")

    def prioritize_targets(self, available_targets: list) -> list:
        return (available_targets)