def fibonacci(n):
    a, b = 0, 1
    sequence = []
    for x in range(n):
        sequence.apend(a)
        a, b = b, a + b
    return sequence

print(fibonacci(5))
