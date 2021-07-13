# shortest common super sequence

# problem statement: Given two strings, output the shortest length of such string which have
# these two strings as subsequence, called as super sequence

# example 1, str1 = xyz, str2 = xyw, output = 4 (xywz) it have both subsequences.
# example 2, str1 = abcdaf, str2 = gcfs, output = 8 (gabcdafs).

# basically it's len(a) + len(b) - LCS(a,b)

def SCS(a, b):
    n = len(a)
    m = len(b)
    matrix = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
    return m + n - matrix[n][m]


str1 = "AGGTAB"
str2 = "GXTXAYB"
print(SCS(str1, str2))
