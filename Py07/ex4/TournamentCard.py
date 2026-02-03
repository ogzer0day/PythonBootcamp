from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable

class TournamentCard(Card, Combatable, Rankable):

    def __init__(self, name: str, card_id: str, rating: int):
        super().__init__(name=name)
        self.card_id = card_id
        self.rating = rating
        self.wins = 0
        self.losses = 0


    def play(self, game_state: dict) -> dict:
        return (game_state)

    def attack(self, target) -> dict:
        return(
            {
                'attacker': self.name,
                'target': target,
                'damage': 5
            }
        )
    def defend(self, attack_points: int) -> int:
        return max(0, attack_points - 2)

    def get_combat_stats(self) -> dict:
        return {"name": self.name, "attack": 5, "defense": 2}

    def get_tournament_stats(self) -> dict:
        return self.play(
            {
                'name': self.name,
                'Id': self.card_id,
                'Interfaces': ['Card', 'Combatable', 'Rankable'],
                'Rating': self.rating,
                'Record': f"{self.wins}-{self.losses}"
            }
        )

    def calculate_rating(self) -> int:
        return (self.rating)
    
    
    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating += 16 * wins
    
    def update_losses(self, losses: int) -> None:
        if self.losses > 0:
            self.losses -= losses
        self.rating -= 16 * losses

    def get_rank_info(self) -> dict:
        return (
            {
                "rating": self.rating,
                "wins": self.wins,
                "losses": self.losses
            }
        )