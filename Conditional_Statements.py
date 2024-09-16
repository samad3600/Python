# Define a variable
x = 10

# if statement
if x > 5:
    print("x is greater than 5")

# if-else statement
if x > 15:
    print("x is greater than 15")
else:
    print("x is not greater than 15")

# if-elif-else statement
if x > 15:
    print("x is greater than 15")
elif x > 5:
    print("x is greater than 5 but not greater than 15")
else:
    print("x is 5 or less")

# Nested if statements
if x > 5:
    if x > 8:
        print("x is greater than 8")
    else:
        print("x is greater than 5 but not greater than 8")
else:
    print("x is 5 or less")

# Ternary operator
result = "x is greater than 5" if x > 5 else "x is 5 or less"
print(result)
