
def mage_counter() -> callable:
    count: int = 0

    def count_call():
        nonlocal count
        count += 1
        return count

    return count_call


def spell_accumulator(initial_power: int) -> callable:
    def accumlates_power():
        nonlocal initial_power
        initial_power += initial_power
        return initial_power

    return accumlates_power

def enchantment_factory(enchantment_type: str) -> callable:
    def ench_appl(enchantment_name: str):
        nonlocal enchantment_type
        return f"{enchantment_type} {enchantment_name}"
    
    return ench_appl

def memory_vault() -> dict[str, callable]:
    memory: dict = {}
    def store(key, value):
        memory[key] = value

    def recall(key):
        return memory.get(key, "Memory not found")
    
    return(
        {
            "store": store,
            "recall": recall
        }
    )

def main():
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