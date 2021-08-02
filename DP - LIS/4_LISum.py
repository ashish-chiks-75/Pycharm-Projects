def LISum(arr):

    n = len(arr)
    lis = [item for item in arr]

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + arr[i]:
                lis[i] = lis[j] + arr[i]

    return max(lis)


lst = [10, 22, 9, 33, 21, 50, 41, 60]
print(LISum(lst))
