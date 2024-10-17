def main():
    # Creating a tuple
    numbers = (1, 2, -5)
    print("Initial tuple:", numbers)

    # Accessing tuple elements
    print("Second element:", numbers[1])

    # Concatenating tuples
    more_numbers = (10, 20)
    combined_tuple = numbers + more_numbers
    print("Combined tuple:", combined_tuple)

    # Checking if an item exists in the tuple
    if 2 in numbers:
        print("2 is in the tuple.")
    else:
        print("2 is not in the tuple.")

    # Iterating through a tuple
    for num in numbers:
        print("Element:", num)

    # Tuple length
    print("Number of elements in the tuple:", len(numbers))

if __name__ == "__main__":
    main()
