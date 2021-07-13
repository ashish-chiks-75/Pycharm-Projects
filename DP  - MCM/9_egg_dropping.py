"""
problem: given e and f as input denoting, number of eggs and number of floors.
Suppose, egg start breaking after k floor, so critical floor will be k.
So, we need to find min number of attempts to find that critical floor in worst case
within given eggs.
like, if we have only one egg, then output should be f because worst case will be critical floor = f
"""
from sys import maxsize as inf


def solve(e, f):

    # base condition
    if e == 1 or f <= 1:
        return f

    # so there will be two cases for each floor, egg will break or not,
    # So one call will be (e-1), (k-1) when egg breaks
    # and second will be e, f-k when egg does not break
    out = inf

    for k in range(1, f+1):

        val = 1 + max(solve(e-1, k-1), solve(e, f-k))
        # max because we need for worst case

        out = min(out, val)
        # min because we need min number of attempts.

    return out


e1 = 3
f1 = 10
print(solve(e1, f1))
