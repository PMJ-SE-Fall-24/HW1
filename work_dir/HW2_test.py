import unittest
from typing import List
from hw2_debugging import merge_sort, recombine  # Replace 'your_module_name' with the name of your Python file without the '.py' extension

class TestMergeSort(unittest.TestCase):

    def test_merge_sort_basic(self):
        self.assertEqual(merge_sort([3, 1, 4, 1, 5, 9]), [1, 1, 3, 4, 5, 9])

    def test_merge_sort_empty(self):
        self.assertEqual(merge_sort([5,7,2,6,9,10]), [2,5,6,7,9,10])

    def test_recombine(self):
        self.assertEqual(recombine([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])

if __name__ == '__main__':
    unittest.main()