def LIS(arr):

    n = len(arr)
    lis = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    return lis


def lbs(arr):
    lis = LIS(arr)
    lds = LIS(list(reversed(arr)))
    lds.reverse()

    ans = 0
    for i in range(len(arr)):
        ans = max(ans, lis[i] + lds[i] - 1)

    return ans


lst = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(lbs(lst))
