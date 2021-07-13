x = "great"
y = "rgeat"
cache = {}


def solve(a, b):
    n = len(a)

    # base condition
    if a == b:
        return True
    if n <= 1:
        return False

    key = a + " " + b
    if key in cache:
        return cache[key]

    # comb1 : assuming they are not swapped at first node level.
    # comb2 : assuming they are swapped at first node level.

    for i in range(1, n):
        comb1 = solve(a[:i], b[:i]) and solve(a[i:], b[i:])
        comb2 = solve(a[:i], b[n-i:]) and solve(a[i:], b[:n-i])
        if comb1 or comb2:
            cache[key] = True
            return True
    cache[key] = False
    return False


print(solve(x, y))
