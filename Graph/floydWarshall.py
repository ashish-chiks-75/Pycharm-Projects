def floydWarshall(graph, n):
    dist = [[graph[q][p] for p in range(n)] for q in range(n)]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist
    
    
V = 6
inf = 10**9
G = [[0, 5, 1, inf, inf, inf],
     [inf, 0, 2, 3, 20, inf],
     [inf, 3, 0, inf, 12, inf],
     [inf, inf, 3, 0, 2, 6],
     [inf, inf, inf, inf, 0, 1],
     [inf, inf, inf, inf, inf, 0]]
print(floydWarshall(G, V))
