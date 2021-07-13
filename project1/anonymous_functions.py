from functools import reduce
X = lambda a: a*a
print(X(5))
Y = lambda a, b: a+b
print(Y(2, 9))

# lambda takes one or more than one argument but takes only one expression.

A = [2, 6, 8, 9, 85, 46, 23, 46, 48]

# filter function
even_list = list(filter(lambda p: p % 2 == 0, A))
print(even_list)

# map function
doubles_list = list(map(lambda q: q*2, A))
print(doubles_list)

# reduce function in functools library
sum_ = reduce(lambda r, s: r+s, A)
print(sum_)

# function to add two list element wise.
A = [4, 5, 6, 7, 8]
B = [1, 2, 5, 9, 10]
C = list(map(lambda q: q[0] + q[1], list(zip(A, B))))
print(C)

# this dic will contain elements and their indexes  as key value pair.
# it can be used where we want to use their indexes, very fastly.
A = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
dic = {a: b for a, b in zip(A, range(len(A)))}
print(dic)


