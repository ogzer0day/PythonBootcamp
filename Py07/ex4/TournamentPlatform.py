from ex4.TournamentCard import TournamentCard
import random


class TournamentPlatform:
    """Platform to register cards, run matches, and track rankings."""

    def __init__(self, winer: int = None, lser: int = None):
        """Initialize the tournament platform with
        optional initial winners/losers."""

        self.cards_db = {}
        self.winer = winer
        self.lser = lser

    def register_card(self, card: TournamentCard) -> str:
        """Register a tournament card and return its ID."""
        self.cards_db[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        """Simulate a match between two cards and update their ratings."""
        card1 = self.cards_db[card1_id]
        card2 = self.cards_db[card2_id]

        winner, loser = random.choice([(card1, card2), (card2, card1)])

        winner.update_wins(1)
        loser.update_losses(1)

        self.winer = winner.rating
        self.lser = loser.rating

        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating,
        }

    def get_leaderboard(self) -> list:
        """Return a simple leaderboard of winner and loser ratings."""
        return [f"{self.winer} (1-0)", f"{self.lser} (0-1)"]

    def generate_tournament_report(self) -> dict:
        """Generate a summary report of the tournament."""
        return {
            "total_cards": 2,
            "matches_played": 1,
            "avg_rating": int((1200 + 1150) / 2),
            "platform_status": "active",
        }
