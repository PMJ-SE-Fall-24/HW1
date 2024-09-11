
import rand
from typing import List


def merge_sort(arr: List[int]) -> List[int]:  # resolving return type error

    if len(arr) == 1:
        return arr

    half = len(arr) // 2

    # print(f'half:{half}') # if printed half the right array returned a none
    # element
    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(leftArr, rightArr):
    leftIndex = 0
    rightIndex = 0
    mergeArr = [0] * (len(leftArr) + len(rightArr))

    while leftIndex < len(leftArr) and rightIndex < len(rightArr):
        if leftArr[leftIndex] < rightArr[rightIndex]:
            mergeArr[leftIndex + rightIndex] = leftArr[leftIndex]
            leftIndex += 1
        else:
            mergeArr[leftIndex + rightIndex] = rightArr[rightIndex]
            rightIndex += 1

    # If there are remaining elements in leftArr
    while leftIndex < len(leftArr):
        mergeArr[leftIndex + rightIndex] = leftArr[leftIndex]
        leftIndex += 1

    # If there are remaining elements in rightArr
    while rightIndex < len(rightArr):
        mergeArr[leftIndex + rightIndex] = rightArr[rightIndex]
        rightIndex += 1

    return mergeArr


arr = rand.random_array([0] * 20)
arr_out = merge_sort(arr)

print(arr_out)


# pip install pyright, pyright <filename>
# autopep8 --in-place --aggressive --aggressive <filename>, pip install autopep8
# install extension of pyright
# pip install pylint, pip install pylint[spelling], pylint <filename>
