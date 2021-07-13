"""
Evaluate Expression to True Boolean Parenthesised
Given a string representing a boolean function, output the number of ways of parenthesising,
so that output is True
OR : |
AND: &
XOR: ^
"""

def solve(s, i, j, c):

    if i == j:
        return int(s[i] == c)

    out = 0

    for k in range(i, j, 2):

        LT = solve(s, i, k, "T")
        LF = solve(s, i, k, "F")
        RT = solve(s, k + 2, j, "T")
        RF = solve(s, k + 2, j, "F")

        if s[k+1] == "|":
            if c == "T":
                out += LT*RT + LF*RT + LT*RF
            else:
                out += LF*RF

        elif s[k+1] == "&":
            if c == "T":
                out += LT*RT
            else:
                out += LF*RF + LF*RT + LT*RF

        else:
            if c == "T":
                out += LT*RF + RT*LF
            else:
                out += LT*RT + LF*RF

    return out


exp = "T|F&T^F"
print(solve(exp, 0, len(exp)-1, "T"))
