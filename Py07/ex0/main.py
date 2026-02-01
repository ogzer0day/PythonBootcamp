from ex0.CreatureCard import CreatureCard


print("=== DataDeck Card Foundation ===\n")

print("Testing Abstract Base Class Desig\n")
print("CreatureCard Info:")
card = CreatureCard(name="Fire Dragon", cost=5, rarity="Legendary",
                    type=None, attack=None, health=None)
info = card.get_card_info()
info["type"] = "Creature"
info["attack"] = 7
info["health"] = 5
print(info, "\n")

print("Playing Fire Dragon with 6 mana available:")
print(f"Player: {card.is_playable(6)}")
result = card.play()

print(f"Play result: {result}\n")

print("Fire Dragon attacks Goblin Warrior:")
res = card.attack_target({
    "attacker": "Fire Dragon",
    "target": "Goblin Warrior",
    "damage_dealt": 7,
    "combat_resolved": True
})
print(f"Attack result: {res}\n")

print("Testing insufficient mana (3 available):")
print(f"Playable: {card.is_playable(3)}\n")

print("Abstract pattern successfully demonstrated!")
