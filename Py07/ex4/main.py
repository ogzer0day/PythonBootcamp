from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform

print("=== DataDeck Tournament Platform ===\n")

card1 = TournamentCard("Fire Dragon", "dragon_001", 1200)
tournament_stats = card1.get_tournament_stats()
print(f"{tournament_stats.get('name')} (ID: {tournament_stats.get('Id')})")
print(f"- Interfaces: {tournament_stats.get('Interfaces')}")
print(f"- Rating: {tournament_stats.get('Rating')}")
print(f"- Record: {tournament_stats.get('Record')}\n")

card2 = TournamentCard("Ice Wizard", "wizard_001", 1150)
tournament_stats = card2.get_tournament_stats()
print(f"{tournament_stats.get('name')} (ID: {tournament_stats.get('Id')})")
print(f"- Interfaces: {tournament_stats.get('Interfaces')}")
print(f"- Rating: {tournament_stats.get('Rating')}")
print(f"- Record: {tournament_stats.get('Record')}\n")

print("Creating tournament match..")
platform = TournamentPlatform()
platform.register_card(card1)
platform.register_card(card2)

print("Creating tournament match...\n")
result = platform.create_match("dragon_001", "wizard_001")

print("Match result:")
print(result)
print()

print("Tournament Leaderboard:")
tournament = platform.get_leaderboard()
if result["winner"] == "dragon_001":
    print(f"1. Fire Dragon - Rating: {tournament[0]}")
    print(f"2. Ice Wizard - Rating: {tournament[1]}\n")
else:
    print(f"1. Ice Wizard - Rating: {tournament[0]}")
    print(f"2. Fire Dragon - Rating: {tournament[1]}\n")

print("Platform Report:")
print(platform.generate_tournament_report())
print()

print(
    "=== Tournament Platform Successfully Deployed! ===\n"
    "All abstract patterns working together harmoniously!"
)
