"""
Given a string, find the length of longest substring which have all
distinct characters.
"""


def distinct_Substring(s):
    n = len(s)
    prev = [-1]*26
    res = 0
    i = 0

    for j in range(n):
        index = ord(s[j]) - ord("a")
        i = max(i, prev[index] + 1)
        res = max(res, j-i+1)
        prev[index] = j

    return res


string = "abcadbd"
print(distinct_Substring(string))
