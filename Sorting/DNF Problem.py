"""
DNF : Dutch national flag problem
Given an array of 0s, 1s and 2s. You need to sort array in O(n) time, O(1) space and in
One traversal of array.
"""


def DNF(arr, n):
    low = 0
    mid = 0
    high = n - 1

    while mid <= high:

        if arr[mid] == 0:
            arr[mid], arr[low] = arr[low], arr[mid]
            low += 1
            mid += 1

        elif arr[mid] == 1:
            mid += 1

        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1


arr = [0, 2, 1, 1, 0, 2, 0, 0, 1, 2]
DNF(arr, len(arr))
print(arr)
