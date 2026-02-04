from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """A card that participates in tournaments with combat and ranking."""

    def __init__(self, name: str, card_id: str, rating: int):
        """Initialize a tournament card with name, ID, and rating."""
        super().__init__(name=name)
        self.card_id = card_id
        self.rating = rating
        self.wins = 0
        self.losses = 0

    def play(self, game_state: dict) -> dict:
        """Play the card without modifying the game state."""
        return game_state

    def attack(self, target) -> dict:
        """Attack a target with a fixed damage."""
        return {"attacker": self.name, "target": target, "damage": 5}

    def defend(self, attack_points: int) -> int:
        """Defend against an attack and reduce damage by 2."""
        return max(0, attack_points - 2)

    def get_combat_stats(self) -> dict:
        """Return the card's combat stats."""
        return {"name": self.name, "attack": 5, "defense": 2}

    def get_tournament_stats(self) -> dict:
        """Return tournament-related stats for the card."""
        return self.play(
            {
                "name": self.name,
                "Id": self.card_id,
                "Interfaces": ["Card", "Combatable", "Rankable"],
                "Rating": self.rating,
                "Record": f"{self.wins}-{self.losses}",
            }
        )

    def calculate_rating(self) -> int:
        """Return the current rating of the card."""
        return self.rating

    def update_wins(self, wins: int) -> None:
        """Update wins and increase rating."""
        self.wins += wins
        self.rating += 16 * wins

    def update_losses(self, losses: int) -> None:
        """Update losses and decrease rating."""
        if self.losses > 0:
            self.losses -= losses
        self.rating -= 16 * losses

    def get_rank_info(self) -> dict:
        """Return ranking information including rating, wins, and losses."""
        return {"rating": self.rating, "wins": self.wins,
                "losses": self.losses}
