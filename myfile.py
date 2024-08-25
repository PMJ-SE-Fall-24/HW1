def fibonacci(n):
    a, b = 0, 1
    sequence = []
    for x in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

print(fibonacci(5))
