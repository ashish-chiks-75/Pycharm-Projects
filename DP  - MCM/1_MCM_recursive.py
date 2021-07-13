"""
MCM: matrix chain multiplication
like if we want to multiply two matrices of dim a*b, c*d necessary condition is
b = c, and the dimension of resulting matrix will be a*d.

In this question, given an array defining matrices in the way like array = [a, b, c, d, e]
So, number of matrices are len(array) - 1, and dim of array are a*b, b*c, c*d, d*e.
And cost of multiplying is defined as mat(a*b) * mat(b*c) = a*b*c.
So, we need to find least cost to find total cost of multiplying all arrays.
i.e, A1*A2*A3*A4 = A
"""
from sys import maxsize as inf


def solve(arr, i, j):

    # base cond: matrix have at least two elements in array
    if i >= j:
        return 0
    out = inf

    for k in range(i, j):
        val = solve(arr, i, k) + solve(arr, k+1, j) + arr[i-1]*arr[k]*arr[j]
        out = min(out, val)

    return out


arr1 = [40, 20, 30, 10, 30]
print(solve(arr1, 1, len(arr1) - 1))
