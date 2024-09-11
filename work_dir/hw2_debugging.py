"""
This module provides an implementation of merge sort algorithm.

It includes the `merge_sort` function to sort a list of integers using the merge sort
algorithm and the `recombine` function to merge two sorted lists into a single sorted list.

Imports:
- List: Type hint for specifying a list of integers.
- rand: Custom module for generating random numbers.

Functions:
- merge_sort(arr: List[int]) -> List[int]: Sorts the input list using merge sort algorithm.
- recombine(left_arr: List[int], right_arr: List[int]) -> List[int]: 
Merges two sorted lists into a single sorted list.
"""
from typing import List
import rand

def merge_sort(arr: List[int]) -> List[int]:  # resolving return type error
    """
    Sorts the input list using the merge sort algorithm.

    This function recursively divides the list into halves, sorts each half, and then
    merges the sorted halves using the `recombine` function.

    Args:
        arr (List[int]): A list of integers to be sorted.

    Returns:
        List[int]: A sorted list of integers.

    Example:
        >>> merge_sort([3, 1, 4, 1, 5, 9])
        [1, 1, 3, 4, 5, 9]
    """

    if len(arr) <= 1:
        return arr

    half = len(arr) // 2

    left_half = arr[:half]
    right_half = arr[half:]

    return recombine(merge_sort(left_half), merge_sort(right_half))



def recombine(left_arr, right_arr):
    """
    Merges two sorted lists into a single sorted list.

    Args:
        left_arr (List[int]): The first sorted list.
        right_arr (List[int]): The second sorted list.

    Returns:
        List[int]: A sorted list containing all elements from left_arr and right_arr.

    Example:
        >>> recombine([1, 3, 5], [2, 4, 6])
        [1, 2, 3, 4, 5, 6]
    """
    left_index = 0
    right_index = 0
    merged_arr = [0] * (len(left_arr) + len(right_arr))

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merged_arr[left_index + right_index] = left_arr[left_index]
            left_index += 1
        else:
            merged_arr[left_index + right_index] = right_arr[right_index]
            right_index += 1

    # If there are remaining elements in left_arr
    while left_index < len(left_arr):
        merged_arr[left_index + right_index] = left_arr[left_index]
        left_index += 1

    # If there are remaining elements in right_arr
    while right_index < len(right_arr):
        merged_arr[left_index + right_index] = right_arr[right_index]
        right_index += 1

    return merged_arr

random_list = rand.random_array([0] * 20)
sorted_list = merge_sort(random_list)

print(sorted_list)


# pip install pyright, pyright <filename>
# autopep8 --in-place --aggressive --aggressive <filename>, pip install autopep8
# install extension of pyright
# pip install pylint, pip install pylint[spelling], pylint <filename>
