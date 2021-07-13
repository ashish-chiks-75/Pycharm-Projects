"""
Given an array, we need to return true or false if this array contains
a subarray of a given sum
"""


def checkSum(arr, x):
    cache = set()
    pre_sum = 0
    for i in arr:
        pre_sum += i
        if pre_sum == x or (pre_sum-x) in cache:
            return True
        cache.add(pre_sum)
    return False


lst = [5, 3, 2, -1, 6]
s = 4
print(checkSum(lst, s))
