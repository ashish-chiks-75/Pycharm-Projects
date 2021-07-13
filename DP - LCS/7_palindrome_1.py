# Longest palindromic subsequence
# print length of largest palindrome subsequence in given string

def palindrome(a):

    # palindrome is LCS between string and its reverse.

    n = len(a)
    b = a[::-1]
    matrix = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if a[i-1] == b[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
    return matrix[n][n]


x = "agbcba"
print(palindrome(x))

# One more question of that min number of deletion or insertion in a string to make a string a
# palindrome is just equal to = len(str) - LCS(str, str.reverse).
