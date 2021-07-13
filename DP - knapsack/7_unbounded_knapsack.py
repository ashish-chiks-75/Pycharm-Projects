# unbounded Knapsack: item can be picked any number of times.
# same as 0 1 knapsack except picked call because it is processed when unpicked, but not processed if picked.

def k(W, wt, val, n):
    K = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if wt[i - 1] <= j:
                K[i][j] = max(val[i - 1] + K[i][j - wt[i - 1]], K[i - 1][j])
            else:
                K[i][j] = K[i - 1][j]
    return K[n][W]


wt1 = [1, 4, 5, 7]
val1 = [1, 5, 7, 8]
W1 = 16
print(k(W1, wt1, val1, len(val1)))
