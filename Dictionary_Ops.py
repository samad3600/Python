def main():
    # Create an initial dictionary
    country_capitals = {
        "Germany": "Berlin",
        "Canada": "Ottawa",
        "England": "London"
    }

    # Accessing values
    print("Capital of Germany:", country_capitals["Germany"])
    print("Capital of England:", country_capitals["England"])

    # Adding an entry
    country_capitals["France"] = "Paris"

    # Updating an entry
    country_capitals["Germany"] = "Bonn"

    # Removing an entry
    del country_capitals["Canada"]

    # Checking key existence
    if "France" in country_capitals:
        print("France is in the dictionary!")

    # Length of the dictionary
    num_entries = len(country_capitals)
    print("Number of entries in the dictionary:", num_entries)

if __name__ == "__main__":
    main()
