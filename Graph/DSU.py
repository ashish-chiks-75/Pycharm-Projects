class DSU:
    def __init__(self, n):
        self.n = n
        self.par = [-1 for _ in range(n)]
        self.rank = [1 for _ in range(n)]
    
    def findPar(self, z):
        if self.par[z] == -1:
            return self.par[z]
        self.par[z] = self.findPar(self.par[z])
        return self.par[z]
    
    def union(self, a, b):
        if self.rank[a] < self.rank[b]:
            a, b = b, a
        self.par[b] = a
        self.rank[a] += int(self.rank[a] == self.rank[b])
