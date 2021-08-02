"""
There are n cities on both side on river numbered increasingly. Given a 2-d lst denoting a bridge should
be built between city lst[i][0] on one side of river and city[i][1] on another side of river.
we need to find max number of bridges that can be built with the condition that
no two bridges should cross each other.
"""


def LIS(arr):

    n = len(arr)
    lis = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    return max(lis)


def bridges(cities):

    cities.sort(key=lambda x: (x[0], x[1]))
    return LIS([i[1] for i in cities])


lst = [[6, 2], [4, 3], [2, 6], [1, 5]]
print(bridges(lst))
