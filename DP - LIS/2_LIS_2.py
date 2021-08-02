def CeilIndex(A, l, r, key):

    while (r - l) > 1:
        m = l + (r - l) // 2
        if A[m] >= key:
            r = m
        else:
            l = m
    return r


def LIS(A, size):

    tailTable = [0 for _ in range(size + 1)]
    l = 1  # always points empty slot
    tailTable[0] = A[0]

    for i in range(1, size):

        if A[i] < tailTable[0]:
            tailTable[0] = A[i]

        elif A[i] > tailTable[l - 1]:
            tailTable[l] = A[i]
            l += 1

        else:
            tailTable[CeilIndex(tailTable, -1, l - 1, A[i])] = A[i]

    return l


lst = [10, 22, 9, 33, 21, 50, 41, 60]
print(LIS(lst, len(lst)))
