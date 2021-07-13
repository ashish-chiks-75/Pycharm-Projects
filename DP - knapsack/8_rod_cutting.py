# problem statement: given two arrays length[i] denoting price[i].
# we have to cut rod in any no of pieces such that price would be max.
# and output the max price.

def rod_cutting(L, len_arr, price, n):

    # same as unbounded knapsack, just L = W.

    K = [[0 for _ in range(L + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, L + 1):
            if len_arr[i-1] <= j:
                K[i][j] = max(price[i - 1] + K[i][j - len_arr[i-1]], K[i - 1][j])
            else:
                K[i][j] = K[i - 1][j]
    return K[n][L]


arr1 = [1, 3, 5, 8, 10]
arr2 = [1, 5, 8, 10, 15]
L1 = 25
print("max profit", rod_cutting(L1, arr1, arr2, len(arr1)))
