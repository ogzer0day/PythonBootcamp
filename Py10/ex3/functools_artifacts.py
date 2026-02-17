from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul

spell_powers = [23, 10, 42, 33, 12, 15]
operations = ['add', 'multiply', 'max', 'min']
fibonacci_tests = [13, 19, 8]

def spell_reducer(spells: list[int], operation: str) -> int:
    if (operation == 'add'):
        return (reduce(add, spells))
    elif (operation == 'multiply'):
        return (reduce(mul, spells))
    elif (operation == 'max'):
        return (reduce(max, spells))
    elif (operation == 'min'):
        return (reduce(min, spells))     
        
def base_enchantment(power, element, target) -> str:
        return f"{element} enchant hits {target} with {power} power!"

def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return(
        {
            'fire_enchant': partial(base_enchantment, 50, "fire"),
            'ice_enchant': partial(base_enchantment, 50, "ice"),
            'lightning_enchant': partial(base_enchantment, 50, "lightning"),
        }
    )

def memoized_fibonacci(n: int) -> int:
    pass

@singledispatch
def spell_dispatcher() -> callable:
    pass


def damage_spell():
    pass

def enchantment():
    pass

def multi_cast():
    pass


def main():
    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(spell_powers, 'add')}")
    print(f"Product: {spell_reducer(spell_powers, 'multiply')}")
    print(f"Max: {spell_reducer(spell_powers, 'max')}\n")

    print("Testing memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(10): {memoized_fibonacci(15)}")

main()