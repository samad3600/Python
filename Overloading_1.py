def print_value(value=None):
    if isinstance(value, int):
        print("Here is int:", value)
    elif isinstance(value, float):
        print("Here is float:", value)
    elif isinstance(value, str):
        print("Here is str:", value)
    else:
        print("No value provided")

print_value(10)       # Calls with int
print_value(10.10)    # Calls with float
print_value("ten")    # Calls with str
print_value()         # Calls with no value
