"""
problem statement: given an integer n, and integer k.
            Suppose n persons are standing in a circular queue numbered from 1 to n.
            Now, starting from 1, every kth person (counting starts from itself) will be
            eliminated. So, output the pos of last person left.

            For example, n = 5, k = 2
            Then first person to die: 2nd
            Then, 4th, 1st, 5th,
            So output will be 3.

            For n = 40, k = 7, output = 24
"""


def solve(n, k):

    if n == 1:
        return 0
    return (solve(n-1,  k) + k) % n


n1, k1 = map(int, input().split())
print("safe position:", solve(n1, k1)+1)
