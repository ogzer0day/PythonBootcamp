from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy

print("=== DataDeck Game Engine ===\n")

print("Configuring Fantasy Card Game...")
game = GameEngine()
factory = FantasyCardFactory()
strategy = AggressiveStrategy()
game.configure_engine(factory, strategy)
print()

print("Simulating aggressive turn...")
rep = game.simulate_turn()
print("Hand:",rep.get("hand"), "\n")

print("Turn execution:")



print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")