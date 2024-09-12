"""fibonacci module"""
def fibonacci(n):
    """fibonacci function"""
    a, b = 0, 1
    sequence = []
    for  _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

print(fibonacci(5))
