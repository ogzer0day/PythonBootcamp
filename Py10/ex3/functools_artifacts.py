from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Callable

spell_powers = [23, 10, 42, 33, 12, 15]
operations = ["add", "multiply", "max", "min"]
fibonacci_tests = [13, 19, 8]


def spell_reducer(spells: list[int], operation: str) -> int:
    """Reduce spell powers using a specified operation."""
    if operation == "add":
        return reduce(add, spells)
    elif operation == "multiply":
        return reduce(mul, spells)
    elif operation == "max":
        return reduce(max, spells)
    elif operation == "min":
        return reduce(min, spells)


def base_enchantment(power, element, target) -> str:
    """Create a base enchantment message."""
    return f"{element} enchant hits {target} with {power} power!"


def partial_enchanter(base_enchantment: Callable) -> dict[str, callable]:
    """Create partially applied enchantment functions."""
    return {
        "fire_enchant": partial(base_enchantment, 50, "fire"),
        "ice_enchant": partial(base_enchantment, 50, "ice"),
        "lightning_enchant": partial(base_enchantment, 50, "lightning"),
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    """Compute Fibonacci numbers using memoization."""
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    """Create a spell dispatcher based on spell type."""

    @singledispatch
    def cast(spell):
        """Handle unknown spell types."""
        return "Unknown spell type"

    @cast.register(int)
    def damage_spel(spell: int):
        """Handle damage spells."""
        return f"Damage spell cast! {spell} damage dealt."

    @cast.register(str)
    def enchantment(spell: str):
        """Handle enchantment spells."""
        return f"Enchantment applied: {spell}"

    @cast.register(list)
    def multi_cast(spell: list):
        """Handle multi-cast spells."""
        return f"Multi-cast activated! Casting {len(spell)} spells."

    return cast


def main():
    """Run tests for reducer and fibonacci functions."""
    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(spell_powers, 'add')}")
    print(f"Product: {spell_reducer(spell_powers, 'multiply')}")
    print(f"Max: {spell_reducer(spell_powers, 'max')}\n")

    print("Testing memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(10): {memoized_fibonacci(15)}")


main()
