# Problem statement : return number of subsets which have equal sum to given input.

def S(arr, n, X):

    # initialization
    c = ([[0 for _ in range(X + 1)] for _ in range(n + 1)])
    for a in range(n + 1):
        c[a][0] = 1

    # similar to knapsack
    for i in range(1, n + 1):
        for j in range(1, X + 1):
            if arr[i-1] <= j:
                c[i][j] = (c[i-1][j-arr[i-1]] + c[i-1][j])
            else:
                c[i][j] = c[i-1][j]
    return c[n][X]


arr1 = [2, 3, 5, 8, 10]
sum_ = 10
print(S(arr1, len(arr1), sum_))

