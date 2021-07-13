"""
Given an unsorted array of integers and a sum.
The task is to count the number of subarray which adds to the given sum.
"""


def countSubarray(arr, x):
    cache = dict()
    pre_sum = 0
    res = 0
    for i in arr:
        pre_sum += i
        res += int(pre_sum == x)
        if (pre_sum - x) in cache:
            res += cache[pre_sum - x]
        if pre_sum in cache:
            cache[pre_sum] += 1
        else:
            cache[pre_sum] = 1
    return res


lst = [10, 5, 2, 7, 1, 9]
s = 15
print(countSubarray(lst, s))

"""
A variation of this problem is given an array, you need to find total sub arrays 
with equal number of zeroes and ones
Ex: [1, 0, 0, 0, 1, 0, 1, 1, 1], output = 8
Solution: So, in this we just need to replace 0 with -1, then the problem will be to find 
total sub arrays with sum 0. 

"""