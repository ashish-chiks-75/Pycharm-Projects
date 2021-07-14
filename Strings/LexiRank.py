"""
Given a string, return the lexicographic rank of string out of
all its permutations.

EX: s = cab, 
permutations = [abc, acb, bac, bca, cab, cba]
Output = 5
"""

from math import factorial


def rightCount(s):
    arr = [0]*26
    res = []
    n = len(s)

    for i in range(n-1, -1, -1):
        index = ord(s[i]) - ord("a")
        arr[index] += 1
        count = 0
        for j in range(index):
            count += arr[j]

        res.append(count)

    return res[::-1]


def lexiRank(string):

    temp = rightCount(string)
    n = len(string)
    rank = 0
    places = factorial(n)

    for i in range(n-1):
        places = places // (n-i)
        rank += (temp[i] * places)

    return rank + 1


txt = "string"
print(lexiRank(txt))
