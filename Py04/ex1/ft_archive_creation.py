
def ft_archive_creation():
    """
        A function that Opening a file in write mode:

            - Creates the file if it doesn't exist
            - Erases and replaces its contents if it already exists
    """
    try:
        print("Initializing new storage unit: new_discovery.txt\n"
              "Storage unit created successfully...\n")
        f = open("new_discovery.txt", "xt")
    except FileExistsError:
        f = open("new_discovery.txt", "wt")
    finally:
        f.write("Inscribing preservation data...\n"
                "{[}ENTRY 001{]} New quantum algorithm discovered\n"
                "{[}ENTRY 002{]} Efficiency increased by 347%\n"
                "{[}ENTRY 003{]} Archived by Data Archivist trainee")
        f.close()


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    ft_archive_creation()

    f = open("new_discovery.txt")
    print(f.read(), "\n")

    print("Data inscription complete. Storage unit sealed.\n"
          "Archive 'new_discovery.txt' ready for long-term preservation.")
