# problem statement: divide the given array into two partitions such that they have min absolute diff.

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
    return c[-1]


arr1 = [5, 11, 6, 4]
z = sum(arr1)
last_row = S(arr1, len(arr1), z//2)
for i in range(len(last_row)-1, -1, -1):
    if last_row[i]:
        print(z-2*i)
        break


