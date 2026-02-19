from typing import Callable

def mage_counter() -> Callable:
    """Create a counter that increments on each call."""
    count: int = 0

    def count_call():
        """Increment and return the call count."""
        nonlocal count
        count += 1
        return count

    return count_call


def spell_accumulator(initial_power: int) -> Callable:
    """Create a function that accumulates spell power."""
    def accumlates_power():
        """Double and return the accumulated power."""
        nonlocal initial_power
        initial_power += initial_power
        return initial_power

    return accumlates_power


def enchantment_factory(enchantment_type: str) -> Callable:
    """Create an enchantment applicator."""
    def ench_appl(enchantment_name: str):
        """Apply an enchantment to a given name."""
        nonlocal enchantment_type
        return f"{enchantment_type} {enchantment_name}"
    
    return ench_appl


def memory_vault() -> dict[str, Callable]:
    """Create a simple key-value memory system."""
    memory: dict = {}

    def store(key, value):
        """Store a value in memory."""
        memory[key] = value

    def recall(key):
        """Retrieve a value from memory."""
        return memory.get(key, "Memory not found")
    
    return(
        {
            "store": store,
            "recall": recall
        }
    )


def main():
    """Run tests for closure-based functions."""
    print("Testing mage counter...")
    call = mage_counter()
    print(f"Call 1: {call()}")
    print(f"Call 2: {call()}")
    print(f"Call 3: {call()}\n")

    print("Testing enchantment factory...")
    enchantment = enchantment_factory("Flaming")
    print(enchantment("Sword"))
    enchantment = enchantment_factory("Frozen")
    print(enchantment("Shield"))


main()
