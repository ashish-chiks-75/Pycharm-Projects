def topological_sort_bfs(n, edges):
    stack = []
    inv = [0]*(n+1)
    vis = [False]*(n+1)
    out = []

    for e in edges:
        inv[e[1]] += 1

    for v in range(1, n+1):
        if inv[v] == 0:
            stack.append(v)

    while stack:
        t = []
        for i in stack:
            out.append(i)
            vis[i] = True

            for j in edges:
                if j[0] == i:
                    inv[j[1]] -= 1

        for k in range(1, n+1):
            if inv[k] == 0 and not vis[k]:
                t.append(k)

        stack = t

    return out


Graph = [[6, 1], [6, 3], [5, 1], [5, 2], [4, 2], [3, 4]]
print(topological_sort_bfs(6, Graph))
