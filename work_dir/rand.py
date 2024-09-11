"""
This module provides functionality for generating a list of random integers using
external system tools.

It includes the `random_array` function which populates a given list with random
integers generated within a specified range using the `shuf` command-line utility.

Imports:
- subprocess: Provides access to system commands for generating random numbers.
- List: Type hint for specifying a list of integers.

Functions:
- random_array(arr: List[int]) -> List[int]: Fills the input list with random integers
  generated using the `shuf` command-line tool.
"""

import subprocess
from typing import List


def random_array(arr: List[int]) -> List[int]:
    """
    Fills the given list with random integers in the range from 1 to 20.

    The function uses the `shuf` command-line tool to generate random numbers.
    It updates the input list `arr` with these random numbers.

    Args:
        arr (List[int]): A list of integers to be populated with random numbers.

    Returns:
        List[int]: The same list `arr`, but with its elements replaced by random integers
        between 1 and 20.

    Example:
        >>> my_list = [0, 0, 0]
        >>> random_array(my_list)
        [15, 8, 12]  # Output will vary as the numbers are random
    """
    shuffled_num = None
    for i,_ in enumerate(arr):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, check=True)
        # stdout returns binary output so changing it to utf-8 decoding method to return int
        arr[i] = int(shuffled_num.stdout.decode("utf-8").strip())
    return arr

# pyright: strict
