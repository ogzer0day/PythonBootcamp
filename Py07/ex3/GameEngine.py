from ex3.CardFactory import CardFactory
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameStrategy import GameStrategy

class GameEngine():
    def configure_engine(self, factory: CardFactory, strategy: GameStrategy) -> None:
        print(f"Factory: {factory.__class__.__name__}")
        print(f"Strategy: {strategy.__class__.__name__}")
        print(f"Available types: {factory.get_supported_types()}")

    def simulate_turn(self) -> dict:
        fact_card = FantasyCardFactory()
        themed_deck = fact_card.create_themed_deck(3)
        print(themed_deck)
        return themed_deck

    def get_engine_status(self) -> dict:
        pass
