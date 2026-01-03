import sys

if __name__ == "__main__":
    print("=== Command Quest ===")

    value: int = 1
    count: int = 1
    len_args: int = len(sys.argv)
    if len_args == 1:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
    else:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {len_args - 1}")

    for value in sys.argv[1:]:
        print(f"Argument {count}: {value}")
        count += 1

    print(f"Total arguments: {len_args}")
