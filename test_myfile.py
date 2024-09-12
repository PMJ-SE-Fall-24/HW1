"""test module"""
import myfile

def test_1():
    """test case 1"""
    assert myfile.fibonacci(5) == [0, 1, 1, 2, 3]

def test_2():
    """test case 2"""
    assert myfile.fibonacci(6) == [0, 1, 1, 2, 3, 5]
