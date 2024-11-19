def primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)) and num > 1:
            primes.append(num)
    return primes

print(primes_in_range(10, 50))  # Output: [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
