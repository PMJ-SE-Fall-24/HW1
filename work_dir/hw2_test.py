"""Test-case module"""
import unittest
from hw2_debugging import merge_sort, recombine

class TestMergeSort(unittest.TestCase):
    """Class"""
    def test_merge_sort_basic(self):
        """
        Test merge_sort with a typical unsorted list.
        """
        self.assertEqual(merge_sort([3, 1, 4, 1, 5, 9]), [1, 1, 3, 4, 5, 9])
    def test_merge_sort_empty(self):
        """
        Test merge_sort with an already sorted list to verify it handles this case correctly.
        """
        self.assertEqual(merge_sort([5, 7, 2, 6, 9, 10]), [2, 5, 6, 7, 9, 10])
    def test_recombine(self):
        """
        Test recombine with two sorted lists to ensure they are merged correctly.
        """
        self.assertEqual(recombine([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])
if __name__ == '__main__':
    unittest.main()
