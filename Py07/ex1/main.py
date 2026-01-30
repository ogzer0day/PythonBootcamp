from ex1.Deck import Deck
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex0.CreatureCard import CreatureCard
from ex0.Card import Card

print("=== DataDeck Deck Builder ===\n")
print("Building deck with different card types...")

spell = SpellCard("Lightning Bolt", 3, "Common", "Deal 3 damage to target")
artifact = ArtifactCard("Mana Crystal", 4, "Permanent: +1 mana per turn",
                        "Common", 2)
creature = CreatureCard("Fire Dragon", 5, "Creature summoned to battlefield",
                        "common", 2, 1)

list_cards: list [Card] = [spell, artifact, creature]

deck = Deck()
for val in list_cards:
    deck.add_card(val)

deck_stat = deck.get_deck_stats()
gamestate = {"gamestate": "common"}

print(f"Deck stats: {deck_stat}\n")

print('Drawing and playing cards:\n')

print(f'Drew: {spell.name} (Spell)')
play_result = spell.play(gamestate)
print(f"Play result: {spell.play(gamestate)}\n")

deck.draw_card()

print(f'Drew: {artifact.name} (Artifact)')
play_result = artifact.play(gamestate)
print(f"Play result: {play_result}\n")

deck.draw_card()

print(f'Drew: {creature.name} (Creature)')
play_result = creature.play(gamestate)
print(f"Play result: {play_result}\n")

deck.draw_card()

print("Polymorphism in action: Same interface, different card behaviors!")
