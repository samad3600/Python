# Original list
my_list = [5, 2, 9, 1, 5, 6]
print(f"Original list: {my_list}")

# Using sort() method
my_list.sort()
print(f"List sorted using sort(): {my_list}")

# Using sorted() function
my_list = [5, 2, 9, 1, 5, 6]  # Resetting the list
sorted_list = sorted(my_list)
print(f"List sorted using sorted(): {sorted_list}")

# Sorting with a custom key (by length)
str_list = ["apple", "banana", "cherry"]
str_list.sort(key=len)
print(f"List sorted by length: {str_list}")

# Sorting in descending order
my_list.sort(reverse=True)
print(f"List sorted in descending order: {my_list}")

# Using lambda function as key
tuple_list = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
tuple_list.sort(key=lambda x: x[1])
print(f"List of tuples sorted by second element: {tuple_list}")
