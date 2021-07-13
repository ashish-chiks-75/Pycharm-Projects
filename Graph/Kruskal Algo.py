from sys import maxsize as inf


def parent(q, arr):
    if arr[q] < 0:
        return q
    return parent(arr[q], arr)


def Kruskal(edges, N):
    t = [-1]*(N+1)
    vis = [0]*len(edges)
    out = []

    while len(out) < (N-1):
        m, k = inf, None
        for i in range(len(edges)):
            if vis[i] == 0 and edges[i][-1] < m:
                k = i
                m = edges[i][-1]
        u = edges[k][0]
        v = edges[k][1]
        p = parent(u, t)
        q = parent(v, t)
        if p != q:
            if t[p] < t[q]:
                t[p] += t[q]
                t[q] = p
            else:
                t[q] += t[p]
                t[p] = q
            out.append([u, v])
        vis[k] = 1
    return out


Graph = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 25, 0, 0, 0, 5, 0],
         [0, 25, 0, 9, 0, 0, 0, 6],
         [0, 0, 9, 0, 10, 0, 0, 0],
         [0, 0, 0, 10, 0, 12, 0, 11],     # 1-indexed graph
         [0, 0, 0, 0, 12, 0, 18, 16],
         [0, 5, 0, 0, 0, 18, 0, 0],
         [0, 0, 6, 0, 11, 16, 0, 0]]

E = []
n = len(Graph)-1
for r in range(1, n+1):
    for o in range(r, n+1):
        if Graph[r][o] != 0:
            E.append([r, o, Graph[r][o]])

res = Kruskal(E, n)
for z in res:
    print(z)
