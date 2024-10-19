# Create a list
my_list = [1, 2, 3, 4, 5]
print(f"Original list: {my_list}")

# Append an element to the list
my_list.append(6)
print(f"List after appending 6: {my_list}")

# Extend the list with another list
my_list.extend([7, 8, 9])
print(f"List after extending: {my_list}")

# Insert an element at a specific position
my_list.insert(2, 'a')  # Insert 'a' at index 2
print(f"List after inserting 'a' at index 2: {my_list}")

# Remove an element by value
my_list.remove(3)  # Removes the first occurrence of 3
print(f"List after removing 3: {my_list}")

# Remove an element by index
removed_element = my_list.pop(1)  # Removes the element at index 1
print(f"List after removing element at index 1: {my_list}, removed element: {removed_element}")

# Find the index of an element
index_of_4 = my_list.index(4)
print(f"Index of element 4: {index_of_4}")

# Sort the list
my_list.sort()
print(f"Sorted list: {my_list}")

# Reverse the list
my_list.reverse()
print(f"Reversed list: {my_list}")

# Slice the list
sub_list = my_list[1:4]  # Gets elements from index 1 to 3
print(f"Sliced list (elements from index 1 to 3): {sub_list}")
