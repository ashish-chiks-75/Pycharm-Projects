# given input a string, output the number of min partition that can turn each partitioned
# into a palindrome.
from sys import maxsize as inf

def palindrome(x):
    for q in range(len(x)//2):
        if x[q] != x[len(x) - 1 - q]:
            return False
    return True

def solve(s, i, j):

    if palindrome(s[i:j+1]):
        return 0

    out = inf

    for k in range(i, j):
        val = solve(s, i, k) + solve(s, k+1, j) + 1
        out = min(out, val)

    return out


str1 = "abcbghhgz"
print(solve(str1, 0, len(str1)-1))
