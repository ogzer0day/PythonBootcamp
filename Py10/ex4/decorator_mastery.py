from typing import Callable
from functools import wraps
import random
import time


def spell_timer(func: Callable) -> Callable:
    """Measure and display execution time of a function."""
    @wraps(func)
    def execution_time(*args, **kwargs):
        """Wrapper that times function execution."""
        start = time.perf_counter()
        print(f"Casting {execution_time.__name__}...")
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Spell completed in {end - start:.3f} seconds")
        return (res)
    
    return (execution_time)


@spell_timer
def timer(var):
    """Return the given value."""
    return (var)


def power_validator(min_power: int) -> Callable:
    """Validate that a spell has sufficient power."""
    def docerator(func):
        """Decorator to enforce minimum power."""
        @wraps(func)
        def check_pow(self, *args, **kwargs):
            """Check spell power before casting."""
            if "power" in kwargs:
                power = kwargs["power"]
            else:
                power = args[1]

            if power < min_power:
                return "Insufficient power for this spell"

            return func(self, *args, **kwargs)
            
        return (check_pow)
    return(docerator)


def retry_spell(max_attempts: int) -> Callable:
    """Retry a spell if it raises an exception."""
    def docerator(func):
        """Decorator to retry failed spell execution."""
        @wraps(func)
        def failed_spells(*argas, **kwargs):
            """Attempt to execute a spell multiple times."""
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
    """Simulate a spell that may randomly fail."""
    if random.random() < 0.7:
        raise ValueError("Random failure occurred!")
    return "Fireball cast successfully!"


class MageGuild:
    """Represent a guild of mages."""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Validate a mage name."""
        if len(name) >= 3 and all(char.isalpha() or char.isspace() for char in name):
            return (True)
        return (False)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast a spell if power is sufficient."""
        print(f"Successfully cast {spell_name} with {power} power")


def main():
    """Run tests for decorators and MageGuild."""
    print("Testing spell timer...")
    print(timer("Fireball cast!"), "\n")

    print('Testing MageGuild...')
    mage_guild = MageGuild()
    print(mage_guild.validate_mage_name("mohamed zougari"))
    print(mage_guild.validate_mage_name("mohamedzo232ugari"))
    mage_guild.cast_spell(spell_name="Lightning", power=15)
    print(mage_guild.cast_spell(spell_name="Lightning", power=2))


main()
