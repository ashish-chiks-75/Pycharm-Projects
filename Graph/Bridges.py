from sys import maxsize as inf


def bridge(graph, v):
    vis = [False] * v
    time = [inf] * v
    low = [inf] * v
    parent = [-1] * v
    curr = 1
    ans = []

    def bridgeUtil(i):
        nonlocal curr
        vis[i] = True
        time[i] = curr
        low[i] = curr
        curr += 1

        for j in range(v):

            if graph[i][j] == 1 and not vis[j]:
                parent[j] = i
                bridgeUtil(j)
                low[i] = min(low[i], low[j])
                if low[j] > time[i]:
                    ans.append([i, j])

            elif graph[i][j] == 1 and j != parent[i]:
                low[i] = min(low[i], time[j])

    bridgeUtil(0)
    return ans


V = 5
G = [[0, 0, 1, 1, 0],
     [1, 0, 0, 0, 0],
     [0, 1, 0, 0, 0],
     [0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0]]

print(bridge(G, V))
