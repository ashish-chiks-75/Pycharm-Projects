"""
Problem 1:
peak element is defined as if a element is greater than both of its neighbours, then
it is a peak element.
Given an array, print index of any one peak element in array

Problem 2:
Bitonic array is defined as increasing then decreasing, so we need to find max element in given
bitonic array.
"""


def solve(arr):

    start = 0
    end = len(arr) - 1

    while start <= end:

        mid = start + (end-start)//2
        if 0 < mid < len(arr) - 1:
            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid
            if arr[mid+1] > arr[mid]:
                start = mid+1
            else:
                end = mid-1
        else:
            if mid == 0:
                return 0
            return len(arr) - 1


lst1 = [10, 8, 6, 9, 12, 16, 18, 20]           # peak element
lst2 = [1, 3, 5, 8, 10, 12, 9, 4, 2]           # bitonic array
print(solve(lst1))
print(solve(lst2))

"""
This code works despite of unsorted array because if arr[mid+1] is greater than arr[mid], then
there is guarantee that right part must contain a peak, if element goes on increasing, then
last index will be answer.
"""