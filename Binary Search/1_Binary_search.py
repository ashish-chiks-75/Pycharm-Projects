# Problem statement: Find index or bool value whether a given number is present
# in given sorted array or not.

def Binary_Search(arr, x):

    start = 0
    end = len(arr) - 1

    while start <= end:

        mid = start + (end - start)//2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1

    return -1


lst = [1, 3, 4, 5, 7, 9, 11, 15]
z = 11
print(Binary_Search(lst, z))

"""
In case binary search does not find any value equal to given value then at the end of loop, 
start and end will point at its neighbours, end will be on its left, and start will be on right.
arr = [a, b, c, d, e, f, g]
and we searched for val which is d < val < e, then at the end of loop, start = index(e) and 
end = index(d).
"""