# problem statement: output the common subsequence as a string in given two strings.


def print_LCS(a, b):
    n = p = len(a)
    m = q = len(b)
    matrix = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

    out = ""
    while p != 0 and q != 0:
        if a[p-1] == b[q-1]:
            out += a[p-1]
            p -= 1
            q -= 1
        else:
            if matrix[p-1][q] > matrix[p][q-1]:
                p -= 1
            else:
                q -= 1
    return out[::-1]


x = "abcdgh"
y = "abedfhr"
print(print_LCS(x, y))
