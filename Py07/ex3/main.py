from ex3.FantasyCardFactory import FantasyCardFactory


print("=== DataDeck Game Engine ===\n")

print("Configuring Fantasy Card Game...")
print("Factory: FantasyCardFactory")
print("Strategy: AggressiveStrategy")

fantasycard = FantasyCardFactory()
print(fantasycard.create_themed_deck(3))


print("Simulating aggressive turn...")


print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")