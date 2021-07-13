n = int(input())
A = [None]*(n+1)
A[0] = 0
A[1] = 1


def fib(x):
    if A[x] is not None:
        return A[x]
    A[x] = fib(x-1) + fib(x-2)
    return A[x]


print(fib(n))


