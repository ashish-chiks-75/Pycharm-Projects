"""
problem statement: Given an array of size n denoting no of books and book[i] contains arr[i] pages,
and given an integer k denoting no of students, So books are to distributed in students
in continuous manner, and output the min number of max pages given.
And each student should get at least one book.

Ex: arr = [10, 30, 20, 50] and k = 2
pairs:           [10], [30, 20, 50]    [10, 30], [20, 50]     [10, 30, 20], [50]  = continuous manner
number of pages:  10,       100           40        70            60        50
max page               100                     70                      60
output = 60
"""


# this function will return min number of students required for all books such that max pages
# will be x
def students(lst, x):
    i = o = 0
    while i < len(lst):
        z = 0
        while i < len(lst) and z + lst[i] <= x:
            z += lst[i]
            i += 1
        o += 1
    return o


# Binary search between max(arr) and sum(arr) as min number of pages would be max(arr) and
# max number of pages would be sum(arr)-min(arr).
# Time complexity = O(n*Log(m)) where n = len(arr) and m = sum(arr)
def solve(arr, k):
    end = 0
    out = -1
    start = m = arr[0]
    for i in arr:
        end += i
        if i > start:
            start = i
        elif i < m:
            m = i
    end -= m

    while start <= end:

        mid = start + (end - start) // 2
        a = students(arr, mid)

        if a <= k:
            out = mid
            end = mid - 1
        else:
            start = mid + 1

    return out


books = [10, 30, 50, 20, 40, 80]
stud = 3
print(solve(books, stud))
