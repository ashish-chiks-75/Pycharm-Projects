# given input a string, output the number of min partition that can turn each partitioned
# in a palindrome.
from sys import maxsize as inf

str1 = "abcbghhgz"
cache = [[-1 for _ in range(len(str1)+1)] for _ in range(len(str1)+1)]

def palindrome(x):
    for q in range(len(x) // 2):
        if x[q] != x[len(x) - 1 - q]:
            return False
    return True


def solve(s, i, j):

    if palindrome(s[i:j+1]):
        cache[i][j] = 0
        return 0

    if cache[i][j] != -1:
        return cache[i][j]

    out = inf

    for k in range(i, j):

        if cache[i][k] == -1:
            cache[i][k] = solve(s, i, k)

        if cache[k+1][j] == -1:
            cache[k+1][j] = solve(s, k+1, j)

        left = cache[i][k]
        right = cache[k+1][j]

        val = 1 + left + right
        out = min(out, val)

    cache[i][j] = out

    return cache[i][j]


print(solve(str1, 0, len(str1)-1))
