"""
Stock span problem: Given an array, return a  output array denoting out[i] as consecutive
smaller or equal values in arr before it.

For example, arr = [1, 4, 2, 6]
So, for i = 0, arr[i] = 1 So, it value will be 1
for i = 1, arr[1] = 4, and arr[0] < arr[1], so its value is 2.
for i = 2, arr[2] = 2, and arr[1] > arr[2], so its value is 1 even though arr[0] is smaller as we need
continuous smaller or equal to it.
for i = 3, arr[3] = 6, So all before ones are smaller, its value will be 4.

So, output = [1, 2, 1, 4]
"""


def solve(arr, n):

    stack = []
    out = [1 for _ in range(n)]
    for i in range(n):

        while stack and stack[-1][0] <= arr[i]:
            out[i] += stack[-1][1]
            stack.pop()

        stack.append([arr[i], out[i]])
        # stack will store element and count of that element.

    return out


lst = [100, 80, 60, 70, 60, 75, 85]
print(solve(lst, len(lst)))

# also, it can be done using concept of Nearest greater to left and just difference between
# indexes of them.
