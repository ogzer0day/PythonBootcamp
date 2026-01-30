from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical

class EliteCard (Card, Combatable, Magical):

    def play(self, game_state: dict) -> dict:
        return (game_state)

    def attack(self, target) -> dict:
        return (
            {
            'attacker': 'Arcane Warrior',
            'target': target,
            'damage': 5,
            'combat_type': 'melee'
            }
        )

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return (
            {
                'caster': 'Arcane Warrior',
                'spell': spell_name,
                'targets': targets,
                'mana_used': 4
            }
        )
    
    def defend(self, incoming_damage: int) -> dict:
        return (
            {
               'defender': 'Arcane Warrior',
               'damage_taken': incoming_damage,
               'damage_blocked': 3,
               'still_alive': True
            }
        )

    def get_combat_stats(self) -> dict:
        return (
            {
            'Attack result': self.attack("Enemy"),
            'Defense result': self.defend(2)
            }
        )

    def channel_mana(self, amount: int) -> dict:
        return ({'channeled': 3, 'total_mana': amount})

    def get_magic_stats(self) -> dict:
        return (
            {
                'Spell cast': self.cast_spell('Fireball',  ['Enemy1', 'Enemy2']),
                'Mana channel': self.channel_mana(7)
            }
        )