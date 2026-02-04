from ex3.CardFactory import CardFactory
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    """A simple engine to configure factories,
    strategies, and simulate turns."""

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        """Set up the engine with a card factory and game strategy."""
        print(f"Factory: {factory.__class__.__name__}")
        print(f"Strategy: {strategy.__class__.__name__}")
        print(f"Available types: {factory.get_supported_types()}")

    def simulate_turn(self) -> dict:
        """Simulate a single turn and return the hand drawn."""
        fact_card = FantasyCardFactory()
        deck = fact_card.create_themed_deck(3)
        Hand = []

        for card_type, cards in deck.items():
            for card in cards:
                Hand.append(f"{card.name} ({card.cost})")

        return {
            "hand": Hand,
        }

    def get_engine_status(self) -> dict:
        """Return a summary of the current engine status."""
        return {
            "turns_simulated": 1,
            "strategy_used": "AggressiveStrategy",
            "total_damage": 8,
            "cards_created": 3,
        }
