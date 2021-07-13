"""
Given a string, output an array having longest consecutive prefix suffix length (lps)
at each index.
lps is defined as length of longest prefix which is also a suffix of that string.
Ex: s: "AABCAA"
suffix: ["", "A", "AA", "CAA", "BCAA", "ABCAA"]
prefix: ["", "A", "AA, "AAB", "AABC", "AABCA"]
output: [0, 1, 0, 0, 1, 2]
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


st = "AAABAAAA"
print(LPS(st))
