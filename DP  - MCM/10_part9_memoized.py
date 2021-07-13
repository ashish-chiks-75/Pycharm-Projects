from sys import maxsize as inf
e1 = 3
f1 = 10
cache = [[-1 for _ in range(f1+1)] for _ in range(e1+1)]

def solve(e, f):

    # base condition
    if e == 1 or f <= 1:
        return f

    if cache[e][f] != -1:
        return cache[e][f]

    # so there will be two cases for each floor, egg will break or not,
    # So one call will be (e-1), (k-1) when egg breaks
    # and second will be e, f-k when egg does not break
    out = inf

    for k in range(1, f+1):

        if cache[e-1][k-1] != -1:
            break_Y = cache[e-1][k-1]
        else:
            break_Y = cache[e-1][k-1] = solve(e-1, k-1)

        if cache[e][f-k] != -1:
            break_N = cache[e][f-k]
        else:
            break_N = cache[e][f-k] = solve(e, f-k)

        val = 1 + max(break_Y, break_N)
        # max because we need for worst case

        out = min(out, val)
        # min because we need min number of attempts.

    cache[e][f] = out

    return out


print(solve(e1, f1))
