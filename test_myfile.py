import myfile

def test_1():
    assert myfile.fibonacci(5) == [0, 1, 1, 2, 3]

def test_2():
    assert myfile.fibonacci(6) == [0, 1, 1, 2, 3, 3]
