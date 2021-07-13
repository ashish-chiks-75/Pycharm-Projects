# problem statement: return bool value such whether a array can be split into two parts with equal sum.

def E(arr):
    if sum(arr) % 2 != 0:
        return False
    return S(arr, len(arr), sum(arr)//2)


# subset sum function.
def S(arr, n, X):

    # initialization
    c = [[False for _ in range(X + 1)] for _ in range(n + 1)]
    for p in range(n + 1):
        c[p][0] = True

    # similar to knapsack
    for i in range(1, n + 1):
        for j in range(1, X + 1):
            if arr[i-1] <= j:
                c[i][j] = (c[i-1][j-arr[i-1]] or c[i-1][j])
            else:
                c[i][j] = c[i-1][j]
    return c[n][X]


list1 = [2, 5, 12, 5, 8, 3, 1]
print(E(list1))
