def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

n = 10  # Number of Fibonacci numbers to generate
fibonacci_sequence = list(fibonacci_generator(n))
print(fibonacci_sequence)