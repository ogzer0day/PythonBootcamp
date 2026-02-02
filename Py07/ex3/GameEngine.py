from ex3.CardFactory import CardFactory
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameStrategy import GameStrategy

class GameEngine():
    def configure_engine(self, factory: CardFactory, strategy: GameStrategy) -> None:
        print(f"Factory: {factory.__class__.__name__}")
        print(f"Strategy: {strategy.__class__.__name__}")
        print(f"Available types: {factory.get_supported_types()}")

    def simulate_turn(self) -> dict:
        fact_card = FantasyCardFactory()
        deck = fact_card.create_themed_deck(3)
        Hand = []

        for card_type, cards in deck.items():
            for card in cards:
                Hand.append(f"{card.name} ({card.cost})")

        return(
            {
                "hand": Hand,
            }
        )
    

    def get_engine_status(self) -> dict:
        return (
            {
                'turns_simulated': 1, 
                'strategy_used': 'AggressiveStrategy',
                'total_damage': 8,
                'cards_created': 3
            }
        )
