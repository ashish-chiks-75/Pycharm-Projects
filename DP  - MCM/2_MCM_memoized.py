from sys import maxsize as inf

lst = [40, 10, 30, 20, 60]
n = len(lst)
t = [[None for _ in range(n+1)] for _ in range(n+1)]

def solve(arr, i, j):

    if i >= j:
        return 0
    if t[i][j] is not None:
        return t[i][j]

    out = inf
    for k in range(i, j):

        if t[i][k] is None:
            t[i][k] = solve(arr, i, k)
        if t[k+1][j] is None:
            t[k+1][j] = solve(arr, k+1, j)

        left = t[i][k]
        right = t[k+1][j]
        temp = left + right + arr[i-1]*arr[k]*arr[j]

        out = min(out, temp)

    t[i][j] = out
    return t[i][j]


print(solve(lst, 1, len(lst)-1))
