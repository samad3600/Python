# Creating a dictionary with initial key-value pairs
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print("Original dictionary:", my_dict)

# Accessing elements using keys
print("Name:", my_dict["name"])
print("Age:", my_dict["age"])

# Adding a new key-value pair
my_dict["email"] = "alice@example.com"
print("Dictionary after adding email:", my_dict)

# Updating an existing key-value pair
my_dict["age"] = 26
print("Dictionary after updating age:", my_dict)

# Removing a key-value pair using pop()
my_dict.pop("city")
print("Dictionary after removing city:", my_dict)

# Removing a key-value pair using del
del my_dict["email"]
print("Dictionary after deleting email:", my_dict)

# Iterating through keys
for key in my_dict:
    print("Key:", key, "Value:", my_dict[key])

# Iterating through key-value pairs
for key, value in my_dict.items():
    print("Key:", key, "Value:", value)

# Checking if a key exists in the dictionary
if "name" in my_dict:
    print("Name is present in the dictionary")
else:
    print("Name is not present in the dictionary")

# Getting all keys
keys = my_dict.keys()
print("Keys:", keys)

# Getting all values
values = my_dict.values()
print("Values:", values)

# Getting all key-value pairs
items = my_dict.items()
print("Items:", items)

# Clearing all elements in the dictionary
my_dict.clear()
print("Dictionary after clearing all elements:", my_dict)
