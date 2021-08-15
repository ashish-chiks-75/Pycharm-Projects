def dfs(graph, i, vis, arr):
    vis[i] = True
    arr.append(i)
    for j in range(len(graph[i])):
        if graph[i][j] == 1 and not vis[j]:
            dfs(graph, j, vis, arr)
    return arr


def sorted_dfs(graph, i, vis, arr):
    vis[i] = True
    for j in range(len(graph[i])):
        if graph[i][j] == 1 and not vis[j]:
            sorted_dfs(graph, j, vis, arr)
    arr.append(i)
    return arr


def transpose(mat, n):
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if mat[i][j]:
                res[j][i] = 1
    return res


def KosaRaju(graph, v):

    lst = sorted_dfs(graph, 0, [False] * v, [])
    rev_graph = transpose(graph, v)
    lst.reverse()

    res = []
    vis = [False] * v
    for i in lst:
        if not vis[i]:
            scc = dfs(rev_graph, i, vis, [])
            res.append(scc)
    return res


# V = 5
# G = [[0, 0, 1, 1, 0],
#      [1, 0, 0, 0, 0],
#      [0, 1, 0, 0, 0],
#      [0, 0, 0, 0, 1],
#      [0, 0, 0, 0, 0]]

V = 4
G = [[0, 1, 0, 0],
     [0, 0, 1, 1],
     [0, 0, 0, 0],
     [1, 0, 0, 0]]

print(KosaRaju(G, V))
