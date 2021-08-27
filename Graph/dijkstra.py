from heapq import heappush, heappop
from sys import maxsize as inf


def dijkstra(graph, n, src):
    vis = [False] * n
    heap = []
    dist = [inf] * n
    dist[src] = 0
    vis[src] = True
    heappush(heap, (0, src))
    
    while heap:
        d, node = heappop(heap)
        vis[node] = True
        for adj, weight in graph[node]:
            if not vis[adj] and d + weight < dist[adj]:
                dist[adj] = d + weight
                heappush(heap, (dist[adj], adj))
        
        # if node == target:
        #     return dist[target]
        
    return dist
    
    
V = 6
G = [[(1, 5), (2, 1)], 
     [(2, 2), (3, 3), (4, 20)], 
     [(1, 3), (4, 12)], 
     [(2, 3), (4, 2), (5, 6)],
     [(5, 1)],
     []
    ]
print(dijkstra(G, V, 0))




    
    