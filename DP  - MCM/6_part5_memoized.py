"""
Evaluate Expression to True Boolean Parenthesised
Given a string representing a boolean function, output the number of ways of parenthesising,
so that output is True
OR : |
AND: &
XOR: ^
"""
str1 = "F|T^T&F"
matrix = [[[-1 for _ in range(len(str1)+1)] for _ in range(len(str1)+1)] for _ in range(2)]

def solve(s, i, j, c):

    if i == j:
        if c:
            return int(s[i] == "T")
        else:
            return int(s[i] == "F")

    if matrix[int(c)][i][j] != -1:
        return matrix[int(c)][i][j]

    out = 0
    for k in range(i, j, 2):

        if matrix[1][i][k] == -1:
            matrix[1][i][k] = solve(s, i, k, True)

        if matrix[0][i][k] == -1:
            matrix[0][i][k] = solve(s, i, k, False)

        if matrix[1][k+2][j] == -1:
            matrix[1][k+2][j] = solve(s, k+2, j, True)

        if matrix[0][k+2][j] == -1:
            matrix[0][k+2][j] = solve(s, k+2, j, False)

        LT = matrix[1][i][k]
        LF = matrix[0][i][k]
        RT = matrix[1][k+2][j]
        RF = matrix[0][k+2][j]

        if s[k + 1] == "|":
            if c:
                out += LT * RT + LF * RT + LT * RF
            else:
                out += LF * RF

        elif s[k + 1] == "&":
            if c:
                out += LT * RT
            else:
                out += LF * RF + LF * RT + LT * RF

        else:
            if c:
                out += LT * RF + RT * LF
            else:
                out += LT * RT + LF * RF

    return out


print(solve(str1, 0, len(str1)-1, True))
