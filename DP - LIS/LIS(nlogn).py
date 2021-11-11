def binSearch(A, start, end, z):
    mid = -1
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == z:
            return -1
        if A[mid] > z:
            end = mid - 1
        else:
            start = mid + 1
    
    return start


def LIS(arr):
    n = len(arr)
    ans = [arr[0]]
    j = 1
    
    for i in range(1, n):
        if arr[i] > ans[-1]:
            ans.append(arr[i])
            j += 1
            continue
        
        pos = binSearch(ans, 0, j-1, arr[i])
        if pos != -1:
            ans[pos] = arr[i]
        
    return j
    
    
print(LIS([2, 3, 8, 7, 11, 9, 10]))
