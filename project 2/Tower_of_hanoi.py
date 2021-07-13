"""
problem statement: given 3 poles named as source, helper, destination and n number of disc are
kept on source pole. So, task is to transfer all disc from source pole to destination pole.
But there are two conditions:
1) You can pick only 1 disc at a time.
2) disc are kept in ascending size, so bigger disc cannot be placed on smaller disc

diagram(for 3 plates):

                        _|_                   |                    |
                      ___|___                 |                    |
                    _____|_____               |                    |

                    Source pole          helper pole          destination pole
"""


def solve(n, s, h, d):

    # base condition
    if n == 1:
        print("move plate {} from pole {} to pole {}".format(n, s, d))
        return

    # Now, we assuming that (n-1) plates are being moved to helper pole recursively.
    solve(n-1, s, d, h)

    # Now we are moving nth plate from source pole to destination pole, and problem became same
    # as previous but s became h and vice-versa.

    print("move plate {} from pole {} to pole {}".format(n, s, d))
    solve(n-1, h, s, d)


solve(4, "s", "h", "d")

"Number of steps will be (2**n -1)"
