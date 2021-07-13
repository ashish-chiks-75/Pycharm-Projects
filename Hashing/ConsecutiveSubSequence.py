"""
Given an array, we need to find longest consecutive subsequence i.e x, x+1, x+2, x+3...
It may appear in any order.

Ex: [1, 9, 3, 4, 8, 5, 2, 11]
output: 5 --> 1, 2, 3, 4, 5
"""


def maxLen(arr):
    s = set(arr)
    ans = 0

    for i in list(s):

        if (i - 1) not in s:
            j = i
            while j in s:
                j += 1
            ans = max(ans, j - i)
    return ans


lst = [1, 9, 3, 4, 8, 5, 2, 11]
print(maxLen(lst))
