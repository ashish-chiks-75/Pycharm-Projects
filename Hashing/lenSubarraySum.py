"""
Given an array, we need to return longest sub array of a given sum.
if no subarray is present, then return -1
"""


def maxLen(arr, x):
    cache = dict()
    pre_sum = 0
    res = -1

    for i in range(len(arr)):
        pre_sum += arr[i]
        if pre_sum == x:
            res = i + 1
        elif (pre_sum - x) in cache:
            res = max(res, i-cache[(pre_sum-x)])

        if pre_sum not in cache:
            cache[pre_sum] = i

    return res


lst = [10, 5, 2, 7, 1, 9]
s = 15
print(maxLen(lst, s))

"""
A variation of this problem is given an array, you need to find longest subarray 
with equal number of zeroes and ones
Ex: [1, 0, 0, 0, 1, 0, 1, 1, 1], output = 8
Solution: So, in this we just need to replace 0 with -1, then the problem will be to find 
longest subarray with sum 0. 

Another variation is given two arrays of equal length, we need to find longest common span with equal sum.
Ex: [2, 3, -1, 4, 5, 8], [10, -2, -1, 3, 6, 15]
output: 3 from index 2 to 4
Solution: longest subarray with sum 0 in array of difference between these two arrays.
"""