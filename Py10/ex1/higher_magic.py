from typing import Callable


def fireball():
    return ("Fireball hits Dragon")

def heal():
    return ("Heals Dragon")

def check_mana(power):
    return (power <= 30)

def base_spell(val):
    return (val)


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(*args, **kwargs):
        result1 = spell1(*args, **kwargs)
        result2 = spell2(*args, **kwargs)
        return (result1, result2)
    
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
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


def spell_sequence(spells: list[Callable]) -> Callable:
    def casts_spells():
        return (spells)
    
    return casts_spells


def main():

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    print(f"Combined spell result: {combined()[0]}, {combined()[1]}\n")

    print("Testing power amplifier...")
    pow_ampl = power_amplifier(base_spell, 2)
    print(f"Original: {10}, Amplified: {pow_ampl(10)}")

main()
