def slopes(arr, n):
    temp = []
    i = 0
    while i < n:
        j = (i + 1)
        res = 0
        while j < n and arr[j] >= arr[j-1]:
            res += (arr[j]-arr[j-1])
            j += 1
        if res != 0:
            temp.append(res)
        i = j
    return temp


lst = [1, 4, 3, 2, 6, 6, 8, 3, 7, 4]
print(slopes(lst, len(lst)))
