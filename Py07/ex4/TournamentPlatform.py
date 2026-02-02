from ex4.TournamentCard import TournamentCard
import random

class TournamentPlatform():

    def register_card(self, card: TournamentCard) -> str:
        pass

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        winner, loser = random((card1_id, card2_id), (card2_id, card1_id))
        winner.update_wins(1)
        loser.update_losses(1)
        return(
            {
                "winner": winner.card_id,
                "loser": loser.card_id,
                "winner_rating": winner.rating,
                "loser_rating": loser.rating
            }
        )

    def get_leaderboard(self) -> list:
        self.create_match()

    def generate_tournament_report(self) -> dict:
        pass