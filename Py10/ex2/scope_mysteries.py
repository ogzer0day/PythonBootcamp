
def mage_counter() -> callable:
    count: int = 0

    def count_call():
        nonlocal count
        count += 1
        return count

    return count_call


def spell_accumulator(initial_power: int) -> callable:
    pass

def enchantment_factory(enchantment_type: str) -> callable:
    pass

def memory_vault() -> dict[str, callable]:
    pass


def main():
    ca = mage_counter()
    print(ca())
    print(ca())
    print(ca())


main()