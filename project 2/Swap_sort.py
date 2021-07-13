"""
Problem statement : Given an array of size n. All element in array are between 1 to n, i.e 1 <= arr[i] <= n
                    and non-repeated, in other words it contain all numbers from 1 to n.
                    But some elements are replaced by some duplicates in that array, we need to find
                    all duplicates and missing numbers.
For example:
             arr = [3, 4, 1, 5, 4, 6, 6, 4]
             Here, missing numbers are [2, 7, 8] and duplicates are [4, 6, 4]

"""

# We can do it easily by using map function in O(n) time and O(n) space complexity, but here
# is the approach for O(n) time complexity and O(1) space complexity.

def swapped_arr(arr, n):
    i = 0
    while i < n:
        pos = arr[i]-1
        if arr[i] == arr[pos]:
            i += 1
        else:
            arr[i], arr[pos] = arr[pos], arr[i]
    return arr


lst = [3, 4, 5, 4, 1, 6, 7, 6, 4]
swapped_lst = swapped_arr(lst, len(lst))
m = []
d = []
for j in range(len(lst)):
    if swapped_lst[j] != j+1:
        m.append(j+1)
        d.append(swapped_lst[j])
print("missing numbers: {}, duplicate numbers: {}".format(m, d))
print(swapped_lst)
