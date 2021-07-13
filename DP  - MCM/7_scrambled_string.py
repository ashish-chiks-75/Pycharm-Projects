# problem statement: given two strings, print bool value if they are scrambled.
# scrambled meaning is that we can break down first string from length except
# empty string, and make a binary tree of each letters.
# Now, we can swap any nodes of tree, if any combination is equal to
# second string, then they are scrambled.

# Example: str1 = great, str2 = ategr, then binary tree will be great
#                                                            1)gr     2)eat
#                                                         3)g   4)r  5)e    6)at
#                                                                         7)a    8)t
#             Now, swap nodes 1 and 2, 5 and 6 to make str1 = str2.
#             hence, they are scrambled string, output = True

def solve(a, b):
    n = len(a)

    # base condition
    if a == b:
        return True
    if n <= 1:
        return False

    # comb1 : assuming they are not swapped at first node level.
    # comb2 : assuming they are swapped at first node level.

    for i in range(1, n-1):
        comb1 = solve(a[:i], b[:i]) and solve(a[i:], b[i:])
        comb2 = solve(a[:i], b[n-i:]) and solve(a[i:], b[:n-i])
        if comb1 or comb2:
            return True
    return False


x = "great"
y = "ategr"
print(solve(x, y))
