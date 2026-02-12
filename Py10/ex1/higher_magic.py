from typing import Callable

test_values = [17, 20, 20]
test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

def fireball(power):
    return (power * 2)

def heal(power):
    return (power)

def check_mana(power):
    return (power <= 30)


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(*args, **kwargs):
        result1 = spell1(*args, **kwargs)
        result2 = spell2(*args, **kwargs)
        return (result1, result2)
    
    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def mage_fireball(*args, **kwargs):
        res = base_spell(*args, **kwargs)
        return (res * multiplier)
    
    return mage_fireball


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def cast(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        else:
            return "Spell fizzled"
        
    return cast




def spell_sequence(spells: list[callable]) -> callable:
    def casts_spells(*args, **kwargs):
        res = spells(*args, **kwargs)
        return (res)
    return 


def main():

    combined = spell_combiner(fireball, heal)
    print(combined(10))

    mega_fireball = power_amplifier(fireball, 3)
    print(mega_fireball(5))

    cast = conditional_caster(check_mana, fireball)
    print(cast(10))
    print(cast(40))


main()
