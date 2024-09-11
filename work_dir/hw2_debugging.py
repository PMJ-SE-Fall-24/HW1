
import rand
from typing import List

def merge_sort(arr: List[int]) -> List[int]: #resolving return type error
    if len(arr) == 1:
        return arr

    half = len(arr) // 2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(leftArr, rightArr):
    leftIndex = 0
    rightIndex = 0
    mergeArr = [None] * (len(leftArr) + len(rightArr))
    while leftIndex < len(leftArr) and rightIndex < len(rightArr):
        if leftArr[leftIndex] < rightArr[rightIndex]:
            rightIndex += 1
            mergeArr[leftIndex + rightIndex] = leftArr[leftIndex]
        else:
            leftIndex += 1
            mergeArr[leftIndex + rightIndex] = rightArr[rightIndex]

    for i in range(rightIndex, len(rightArr)):
        mergeArr[leftIndex + rightIndex] = rightArr[i]
    for i in range(leftIndex, len(leftArr)):
        mergeArr[leftIndex + rightIndex] = leftArr[i]

    return mergeArr


arr = rand.random_array([None] * 20)
arr_out = merge_sort(arr)

print(arr_out)


# pip install pyright, pyright <filename>
# autopep8 --in-place --aggressive --aggressive <filename>, pip install autopep8
# install extension of pyright
# pip install pylint, pip install pylint[spelling], pylint <filename>
