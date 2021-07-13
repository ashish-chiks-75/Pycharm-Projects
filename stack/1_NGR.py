# NGR: Nearest greatest element from right.
# given an array, output the array which contains nearest greater element of that pos.
# For example : arr = [1, 3, 2, 4], then for 1, all other are greater, but nearest is 3.
# So, for 1, out = 3, for 3, out = 4, hence output = [3, 4, 4, -1].


def NGR(arr):

    stack = []
    out = []
    for i in range(len(arr)-1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            out.append(stack[-1])
        else:
            out.append(-1)
        stack.append(arr[i])

    return out[::-1]


lst = [1, 5, 7, 6, 9, 3, 4]
print(NGR(lst))
