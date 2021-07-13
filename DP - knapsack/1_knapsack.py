# Problem statement: pick items from given array which don't exceeds max limit and have max value.

weights1 = [1, 4, 5, 9]
values1 = [1, 5, 7, 10]
W1 = 10
n1 = len(values1)

# memoization
"""
c = [[-1 for _ in range(W1 + 1)] for _ in range(n1 + 1)]
def k(weights, values, W, n):
    
    if c[n][W] != -1:
        return c[n][W]
    if n == 0 or W == 0:
        return 0

    if weights[n-1] > W:
        c[n][W] = k(weights, values, W, n-1)
    else:
        c[n][W] = max(k(weights, values, W, n-1), k(weights, values, W - weights[n-1], n-1) + values[n-1])
    return c[n][W]


print(k(weights1, values1, W1, n1))
"""

# bottom-up approach
"""
def k(W, wt, val, n):
    K = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if wt[i - 1] <= j:
                K[i][j] = max(val[i - 1] + K[i - 1][j - wt[i - 1]], K[i - 1][j])
            else:
                K[i][j] = K[i - 1][j]
    return K[n][W]


print(k(W1, weights1, values1, n1))
"""
