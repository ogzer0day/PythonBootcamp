from typing import Callable
from functools import wraps
import time

def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def execution_time(*args, **kwargs):

        start = time.perf_counter()
        print(f"Casting {execution_time.__name__}...")
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Spell completed in {end - start:.3f} seconds")
        return (res)
    
    return (execution_time)


@spell_timer
def timer(var):
    return (var)



def power_validator(min_power: int) -> Callable:
    pass


def retry_spell(max_attempts: int) -> Callable:
    pass


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        pass

    def cast_spell(self, spell_name: str, power: int) -> str:
        pass


def main():
    print("Testing spell timer...")
    print(timer("Fireball cast!"), "\n")

main()