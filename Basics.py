print("Hello, World!")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
sum_result = num1 + num2
print(f"The sum is: {sum_result}")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a positive integer: "))
print(f"Factorial of {num} is {factorial(num)}")
