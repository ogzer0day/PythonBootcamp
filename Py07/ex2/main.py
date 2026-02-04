from ex2.EliteCard import EliteCard

print("=== DataDeck Ability System ===\n")
print("EliteCard capabilities:")

print("- Card: ['play', 'get_card_info', 'is_playable']")
print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']\n")

print("laying Arcane Warrior (Elite Card):\n")

combat = EliteCard()

print("Combat phase:")
for key, val in combat.get_combat_stats().items():
    print(f"{key}: {val}")

print()
print("Magic phase:")
for key, val in combat.get_magic_stats().items():
    print(f"{key}: {val}")

print()
print("Multiple interface implementation successful!")
