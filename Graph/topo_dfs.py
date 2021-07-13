def topological_sort_dfs(n, graph):
    visited = [False for _ in range(n+1)]
    result = []

    def DFS(node):
        if visited[node]:
            return
        visited[node] = True
        for i in graph:
            if i[0] == node:
                DFS(i[1])
        result.append(node)

    for j in range(1, n+1):
        DFS(j)

    return list(reversed(result))


Graph = [[6, 1], [6, 3], [5, 1], [5, 2], [4, 2], [3, 4]]
print(topological_sort_dfs(6, Graph))
