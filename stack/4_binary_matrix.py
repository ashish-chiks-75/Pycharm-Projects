"""
Problem statement: Given a 2 D array of only one and zeroes, output the maximum area of rectangle
in matrix which only contains 1
"""

def MAH(histogram):
    stack = list()
    max_area = 0
    index = 0
    while index < len(histogram):

        if (not stack) or (histogram[stack[-1]] <= histogram[index]):
            stack.append(index)
            index += 1

        else:
            top_of_stack = stack.pop()
            area = (histogram[top_of_stack] * ((index - stack[-1] - 1) if stack else index))

            max_area = max(max_area, area)

    while stack:
        top_of_stack = stack.pop()
        area = (histogram[top_of_stack] *
                ((index - stack[-1] - 1)
                 if stack else index))

        max_area = max(max_area, area)

    return max_area


def solve(matrix, n, m):
    histogram = [a for a in matrix[0]]
    res = MAH(histogram)
    for i in range(1, n):
        for j in range(m):
            if matrix[i][j] == 1:
                histogram[j] += matrix[i][j]
            else:
                histogram[j] = 0
        res = max(res, MAH(histogram))
    return res


mat = [[0, 1, 1, 0],
       [1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 1, 0],
       [0, 1, 1, 1]]
print(solve(mat, len(mat), len(mat[0])))
