# problem statement: min number of insertion and deletion in string a to make
# it as string b.

# string a ____deletion_______ LCS(str a, str b) ______insertion_________string b


def LCS(a, b):
    n = len(a)
    m = len(b)
    matrix = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
    return matrix[n][m]


x = "heap"
y = "pea"
result = LCS(x, y)
print("min number of deletions:", len(x) - result)
print("min number of insertions: ", len(y) - result)
