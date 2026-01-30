from ex3.CardFactory import CardFactory
from ex0.Card import Card
class FantasyCardFactory(CardFactory, Card):
    def create_creature(self, name_or_power) -> Card:
        return (
            
        )
    
    def create_spell(self, name_or_power) -> Card:
        pass
    
    def create_artifact(self, name_or_power) -> Card:
        pass
    
    def create_themed_deck(self, size: int) -> dict:
        pass
    
    def get_supported_types(self) -> dict:
        pass