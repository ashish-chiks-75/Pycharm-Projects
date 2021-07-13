# problem statement: output the max number of ways by which we can make a sum of given input by
# given array of coins

# just same as count subset sum, except picking element one time.
# so, variation is same as from 01 knapsack to unbounded knapsack.

def C(arr, n, X):

    # initialization
    c = ([[0 for _ in range(X + 1)] for _ in range(n + 1)])
    for a in range(n + 1):
        c[a][0] = 1

    # similar to unbounded knapsack
    for i in range(1, n + 1):
        for j in range(1, X + 1):
            if arr[i-1] <= j:
                c[i][j] = (c[i][j-arr[i-1]] + c[i-1][j])
            else:
                c[i][j] = c[i-1][j]
    return c[n][X]


arr1 = [1, 2, 3]
x1 = 4
print(C(arr1, len(arr1), x1))
