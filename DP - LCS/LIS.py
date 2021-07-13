def LIS(arr):
    A = [1]*len(arr)
    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[i] > arr[j] and A[i] < (A[j] + 1):
                A[i] = A[j] + 1
    return max(A)


lst = list(map(int, input().split()))
print(LIS(lst))
