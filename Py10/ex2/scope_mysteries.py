
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
    pass


def main():
    ca = mage_counter()
    print(ca())
    print(ca())
    print(ca())

    print()
    acp = spell_accumulator(2)
    print(acp())
    print(acp())
    print(acp())

    print()
    ench = enchantment_factory("Flaming")
    print(ench("Sword"))

main()