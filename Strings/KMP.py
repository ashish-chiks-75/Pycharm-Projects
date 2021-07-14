"""
Given two string, find all indexes of str1 after which all characters of
str2 appears consecutively in str1. OR
Find the indexes at which str2 matches str1

Ex: str1 = str1 = "cabbcdababbc", str2 = "abb"
Output: [1, 8]
"""


def LPS(s):
    n = len(s)
    lps = [0] * n
    l = 0
    i = 1

    while i < n:
        if s[i] == s[l]:
            l = l + 1
            lps[i] = l
            i = i + 1
        else:
            if l != 0:
                l = lps[l - 1]
            else:
                lps[i] = 0
                i = i + 1

    return lps


def KMP(s, pattern):
    n = len(s)
    m = len(pattern)
    lps = LPS(pattern)
    i, j = 0, 0
    res = []

    while i < n:
        if pattern[j] == s[i]:
            i += 1
            j += 1
        if j == m:
            res.append(i-j)
            j = lps[j-1]
        elif i < n and pattern[j] != s[i]:
            if j == 0:
                i += 1
            else:
                j = lps[j-1]

    return res


str1 = "cabbcdababbc"
str2 = "abb"
print(KMP(str1, str2))
