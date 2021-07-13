"""
Given an array of integers, we need to return true or false if array have
a pair with a given sum.
"""


def isPair(arr, x):
    cache = set()
    for i in arr:
        if (x-i) in cache:
            return True
        cache.add(i)
    return False


lst = [8, 3, 4, 2, 5]
s = 6
print(isPair(lst, s))
