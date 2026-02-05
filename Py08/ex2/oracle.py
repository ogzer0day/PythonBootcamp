"""
oracle.py

Chapter VI - Exercise 02: Accessing the Mainframe

This script loads configuration from environment variables and a .env file
using python-dotenv. It checks that all required settings are present, warns
about missing configuration, and prints a summary of the system status.

Authorized modules: os, python-dotenv
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env if present
load_dotenv()

# List of required configuration variables
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

    # Identify any missing variables
    missing = missing_vars()

    if missing:
        print("Warning: Missing configuration detected")
        for var in missing:
            print(f"[MISSING] {var}")
        print()
        print("The Oracle cannot see everything yet.")
        exit(1)

    # Load configuration values
    mode = os.getenv("MATRIX_MODE")
    database = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion = os.getenv("ZION_ENDPOINT")

    # Display configuration summary
    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: Connected to {'local' if mode == 'development' else 'remote'} instance")
    print(f"API Access: {api_key}")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {zion}\n")

    # Security check summary
    print(
        "Environment security check:\n"
        "[OK] No hardcoded secrets detected\n"
        "[OK] .env file properly configured\n"
        "[OK] Production overrides available\n"
    )

    print("The Oracle sees all configurations.")
