# Euclidean theorem for gcd.
def gcd(a, b):
    if a == b:
        return a
    else:
        if a > b:
            a = a-b
        else:
            b = b-a
        return gcd(a, b)


print(gcd(1491, 952))