from typing import Callable
from functools import wraps
import random
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

    def docerator(func):

        @wraps(func)
        def check_pow(pow, *args, **kwargs):
            if (pow < min_power):
                return ("Insufficient power for this spell")
            else:
                return (func(pow, *args, **kwargs))
            
        return (check_pow)
    return(docerator)

@power_validator(15)
def validator_pow(pow, spell_name):
    print(f"Successfully cast {spell_name} with {pow} power")


def retry_spell(max_attempts: int) -> Callable:
    
    def docerator(func):
        @wraps(func)
        def failed_spells(*argas, **kwargs):

            for n in range(max_attempts):
                try:    
                    return func(*argas, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... (attempt {n}/{max_attempts})")

            return f"Spell casting failed after {max_attempts} attempts"
        return failed_spells
    return docerator


@retry_spell(3)
def check_failed():
    if random.random() < 0.7:
        raise ValueError("Random failure occurred!")
    return "Fireball cast successfully!"


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        pass

    def cast_spell(self, spell_name: str, power: int) -> str:
        pass


def main():
    print("Testing spell timer...")
    print(timer("Fireball cast!"), "\n")

    print("Testing MageGuild...")
    validator_pow(15, "lightning")
    print(validator_pow(2, "lightning"), "\n")

    print("test failed spells")
    print(check_failed())

main()