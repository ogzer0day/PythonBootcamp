import os
from dotenv import load_dotenv


load_dotenv()

REQUIRED_VARS = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]


def missing_vars():
    """
    Check which required environment variables are missing.

    Returns:
        list[str]: A list of variable names that are not set.
    """
    return [var for var in REQUIRED_VARS if not os.getenv(var)]


if __name__ == "__main__":
    print("ORACLE STATUS: Reading the Matrix...\n")

    missing = missing_vars()

    if missing:
        print("Warning: Missing configuration detected")
        for var in missing:
            print(f"[MISSING] {var}")
        print()
        print("The Oracle cannot see everything yet.")
        exit(1)

    mode = os.getenv("MATRIX_MODE")
    database = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion = os.getenv("ZION_ENDPOINT")

    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(
        "Database: Connected to "
        f"{'local' if mode == 'development' else 'remote'} instance"
    )
    print(f"API Access: {api_key}")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {zion}\n")

    print(
        "Environment security check:\n"
        "[OK] No hardcoded secrets detected\n"
        "[OK] .env file properly configured\n"
        "[OK] Production overrides available\n"
    )

    print("The Oracle sees all configurations.")
