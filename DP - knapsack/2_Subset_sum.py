# problem statement: return bool value whether a subset of an array can be created such that its sum
# is equal to given input.

def S(arr, n, X):

    # initialization
    c = [[False for _ in range(X + 1)] for _ in range(n + 1)]
    for p in range(n+1):
        c[p][0] = True

    # similar to knapsack
    for i in range(1, n + 1):
        for j in range(1, X + 1):
            if arr[i-1] <= j:
                c[i][j] = c[i-1][j-arr[i-1]] or c[i-1][j]
            else:
                c[i][j] = c[i-1][j]
    return c[n][X]


arr1 = [6, 3, 1, 10]
print(S(arr1, 4, 12))



