"""
Given two string str1 and str2, we need to find minimum no of operations on
str1 to convert it into str2.
operations: delete, insert, replace
"""


def editDistDP(str1, str2, m, n):

    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for a in range(1, m+1):
        dp[a][0] = a
    for b in range(1, n+1):
        dp[0][b] = b

    for i in range(m + 1):
        for j in range(n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

    return dp[m][n]


s1 = "ashish"
s2 = "ashwinx"

print(editDistDP(s1, s2, len(s1), len(s2)))
