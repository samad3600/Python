def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

n = int(input("Enter the number of terms: "))
print(f"Fibonacci sequence: {fibonacci(n)}")
