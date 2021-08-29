from heapq import heappush, heappop


def primsMST(graph, n, start=0):
    vis = [False] * n
    heap = []
    count = 0
    total = 0
    ans = []
    vis[start] = True
    for i, j in graph[start]:
        heappush(heap, (j, start, i))

    while count < (n-1) and heap:
        weight, fr, to = heappop(heap)
        if vis[to]:
            continue
        vis[to] = True
        ans.append([fr, to])
        total += weight
        count += 1

        for adj, w in graph[to]:
            if not vis[adj]:
                heappush(heap, (w, to, adj))

    if count != (n - 1):
        return -1, -1
    return total, ans


V = 9
G = [[(1, 4), (7, 8)],
     [(0, 4), (2, 8), (7, 11)],
     [(1, 8), (3, 7), (5, 4), (8, 2)],
     [(2, 7), (4, 9), (5, 14)],
     [(3, 9), (5, 10)],
     [(2, 4), (3, 14), (4, 10), (6, 2)],
     [(5, 2), (7, 1), (8, 6)],
     [(0, 8), (1, 11), (6, 1), (8, 7)],
     [(2, 2), (6, 6), (7, 7)]]

print(primsMST(G, V))
