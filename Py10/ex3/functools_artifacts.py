from functools import reduce, partial
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
        

def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    pass

def memoized_fibonacci(n: int) -> int:
    pass

def spell_dispatcher() -> callable:
    pass


def main():
    print(spell_reducer(spell_powers, 'multiply'))
    print()



main()