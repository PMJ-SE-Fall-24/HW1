def fibonacci(n):
    a, b = 0, 1
    sequence = []
    for x in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

terms = input("Enter the number of terms: ")
print(f"Fibonacci sequence up to {terms} terms:")
print(fibonacci(terms))