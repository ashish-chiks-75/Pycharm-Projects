# longest repeating subsequence
# problem statement: output the max length of repeating subsequence in a given strings.

# example: str = AABCBEDD, output = 3, (ABD)


def L(a, b):

    # we are passing same string as two diff input, but finding LCS with restriction that
    # index should not be same for two letters.
    n = len(a)
    matrix = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if a[i-1] == b[j-1] and i != j:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
    return matrix[n][n]


x = "AABCBEDD"
print(L(x, x))
