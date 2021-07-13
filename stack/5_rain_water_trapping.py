"""
problem statement: Given an array denoting height of consecutive blocks.
Output the max amount of water that can be stored between them.

For example, input: [3, 1, 4]
Then blocks be like :
                                          ______
                       ______             ______
                       ______             ______
                       ______    ______   ______
So, water be stored above 2 block and height will be 2 units.
So, amount = 2*1 = 2 = output
"""


def max_left(arr, n):

    out = []
    ml = arr[0]
    for i in range(1, n-1):
        out.append(ml)
        ml = max(ml, arr[i])
    return out


def solve(arr, n):

    Max_left = max_left(arr, n)
    Max_right = max_left(arr[::-1], n)[::-1]
    res = 0

    for i in range(1, n-1):
        res += max(min(Max_left[i-1], Max_right[i-1]) - arr[i], 0)

    return res


lst = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(solve(lst, len(lst)))
