import sys
import os
import site

def out_of_venv():
    venv_path = os.environ.get("VIRTUAL_ENV")

    print("MATRIX STATUS: You're still plugged in\n")

    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {venv_path} detected\n")

    print("WARNING: You're in the global environment!\n"
          "The machines can see everything you install.")

    print(
          "To enter the construct, run:\n"
          "python -m venv matrix_env\n"
          "source matrix_env/bin/activate # On Unix\n"
          "matrix_env\n"
          "Scripts\n"
          "activate     # On Windows\n"
          "Then run this program again."
        )

def in_venv():
    venv_path = os.environ.get("VIRTUAL_ENV")
    site_packages_paths = site.getsitepackages()

    print("MATRIX STATUS: Welcome to the construct\n")

    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: matrix_env")
    print(f"Environment Path: {venv_path}\n")

    print(
          "SUCCESS: You're in an isolated environment!\n"
          "Safe to install packages without affecting\n"
          "the global system\n"
        )
    
    print("Package installation path:")
    print(site_packages_paths[0])

if __name__ == "__main__":

    if sys.prefix != sys.base_prefix:
        in_venv()
    else:
        out_of_venv()