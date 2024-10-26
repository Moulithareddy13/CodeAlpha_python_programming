def fibonacci_generator(n):
    fibonacci_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence

# Example usage
n = 10  # Number of terms you want
print(fibonacci_generator(n))
