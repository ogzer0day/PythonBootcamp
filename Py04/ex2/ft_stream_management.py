import sys


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    stdin_vr = input("Input Stream active. Enter archivist ID: ")
    stdin_vr2 = input("Input Stream active. Enter status report: ")

    print()

    sys.stdout.write(f"{'{[}STANDARD{]}'} Archive status {stdin_vr}: "
                     f"{stdin_vr2}\n")

    sys.stderr.write(f"{'{[}ALERT{]}'} System diagnostic: "
                     f"Communication channels verified\n")

    sys.stdout.write(f"{'{[}STANDARD{]}'} Data transmission complete\n")

    print()

    print("Three-channel communication test successful.")
