
if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    print("nitiating secure vault access...\n"
          "Vault connection established with failsafe protocols\n")

    print("SECURE EXTRACTION:")
    with open("classified_data.txt", "r") as f:
        print(f.read(), "\n")

    print("SECURE PRESERVATION:")
    with open("classified_data.txt", "w") as d:
        d.write("{[}CLASSIFIED{]} New security protocols archived\n"
                "Vault automatically sealed upon completion")

    with open("classified_data.txt") as e:
        print(e.read(), "\n")

    print("All vault operations completed with maximum security.")
