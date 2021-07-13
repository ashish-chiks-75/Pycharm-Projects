# Problem: Given a graph in matrix form, output the order of edges
# which gives the minimum cost spanning tree.

from sys import maxsize as I
from typing import List


def Prim(G, n):
    near = [I for _ in range(n+1)]
    vis: List[List[int]] = [[0, 0] for _ in range(n-1)]
    m = I
    u, v = 1, 1

    for i in range(1, n+1):
        for j in range(i, n+1):
            if G[i][j] < m:
                m = G[i][j]
                u, v = i, j
    vis[0][0] = u
    vis[0][1] = v
    near[u] = 0
    near[v] = 0

    for i in range(1, n+1):
        if near[i] != 0:
            if G[i][u] < G[i][v]:
                near[i] = u
            else:
                near[i] = v

    for i in range(1, n-1):
        m = I
        for j in range(1, n+1):
            if near[j] != 0 and G[j][near[j]] < m:
                m = G[j][near[j]]
                k = j
        vis[i][0] = near[k]
        vis[i][1] = k
        near[k] = 0

        for t in range(1, n+1):
            if near[t] != 0 and G[t][k] < G[t][near[t]]:
                near[t] = k
    return vis


Graph = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, I, 25, I, I, I, 5, I],
         [0, 25, I, 9, I, I, I, 6],
         [0, I, 9, I, 10, I, I, I],
         [0, I, I, 10, I, 12, I, 11],     # 1-indexed graph
         [0, I, I, I, 12, I, 18, 16],
         [0, 5, I, I, I, 18, I, I],
         [0, I, 6, I, 11, 16, I, I]]
res = Prim(Graph, len(Graph)-1)
for i in res:
    print(i)
