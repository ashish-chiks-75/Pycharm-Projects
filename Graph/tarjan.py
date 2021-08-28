def tarjan(graph, n):
    low = [-1] * n
    time = [-1] * n
    onStack = [False] * n
    stack = []
    ans = []
    t = 1

    def dfs(curr):
        nonlocal t
        time[curr] = t
        low[curr] = t
        stack.append(curr)
        onStack[curr] = True
        t += 1

        for adj in graph[curr]:
            if time[adj] == -1:
                dfs(adj)
                low[curr] = min(low[curr], low[adj])
            elif onStack[adj]:
                low[curr] = min(low[curr], time[adj])

        if time[curr] == low[curr]:
            scc = []
            next_node = -1
            while next_node != curr:
                next_node = stack.pop()
                scc.append(next_node)
                onStack[next_node] = False
            ans.append(scc)

    for i in range(n):
        if time[i] == -1:
            dfs(i)
    return ans


V = 8
G = [[1, 2],
     [0, 3],
     [3],
     [4, 5],
     [2, 5, 6],
     [7],
     [5],
     [6]]

print(tarjan(G, V))
