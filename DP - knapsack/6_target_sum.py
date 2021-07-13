# problem statement: given an array, we have to assign + or - sign to each element in array,
# such that the sum of array becomes given input and output the number of ways to do it.

def T(arr, x):
    # s1 + s2 = sum(arr)
    # s1 - s2 = x
    # s2 = (sum(arr) - x)//2

    if (sum(arr) - x) % 2 != 0:
        return 0
    return S(arr, len(arr), (sum(arr)-x)//2)


# count subset sum function.
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


arr1 = [1, 1, 2, 3]
x1 = 1
print(T(arr1, x1))
