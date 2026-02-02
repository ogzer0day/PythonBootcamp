from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform

print("=== DataDeck Tournament Platform ===\n")

card1 = TournamentCard("Fire Dragon", "dragon_001", 1200, 0, 0)
tournament_stats = card1.get_tournament_stats()
print(f"{tournament_stats.get('name')} (ID: {tournament_stats.get('Id')})")
print(f"-  Interfaces: {tournament_stats.get('Interfaces')}")
print(f"- Rating: {tournament_stats.get('Record')}")


print("=== Tournament Platform Successfully Deployed! ===\n"
    "All abstract patterns working together harmoniously!")