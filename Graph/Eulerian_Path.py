def isEulerianPath(graph, n, outDeg, inDeg):
    for i in range(n):
        outDeg[i] = len(graph[i])
        for j in graph[i]:
            inDeg[j] += 1
    
    start = 0
    for node in range(n):
        z = outDeg[node] - inDeg[node]
        if z > 1 or z < -1:
            return False, start
        if z == 1:
            if start != 0:
                return False, start
            start = node
    return True, start
    
    
def dfs(graph, ans, curr, outDeg):
    
    while outDeg[curr]:
        outDeg[curr] -= 1
        adj = graph[curr][outDeg[curr]]
        dfs(graph, ans, adj, outDeg)
        
    ans.append(curr)
    
    
def eulerianPath(graph, n):
    inDeg = [0] * n
    outDeg = [0] * n
    flag, start = isEulerianPath(graph, n, outDeg, inDeg)
    if not flag:
        return -1
    solution = []
    dfs(graph, solution, start, outDeg)
    solution.reverse()
    return solution
    
    
V = 6
G = [[3],
     [0, 2],
     [1, 0, 4],
     [2],
     [5],
     [2]]
print(eulerianPath(G, V))
