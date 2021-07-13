def detonation(r, c, grid):
    A = []
    for i in range(r):
        for j in range(c):
            if grid[i][j] == "O":
                A.append([i, j])
            grid[i][j] = "O"
    for a in range(len(A)):
        x = A[a][0]
        y = A[a][1]
        grid[x][y] = "."
        if x + 1 <= (r - 1):
            grid[x+1][y] = "."
        if (x - 1) >= 0:
            grid[x-1][y] = "."
        if y + 1 <= (c - 1):
            grid[x][y+1] = "."
        if (y - 1) >= 0:
            grid[x][y-1] = "."
    return grid

def bomberMan(n, grid, r, c):
    if n <= 3:
        if n == 1:
            return grid
        elif n == 2:
            for i in range(r):
                for j in range(c):
                    grid[i][j] = "O"
            return grid
        else:
            grid = detonation(r, c, grid)
            return grid
    else:
        grid = detonation(r, c, grid)
        N = n - 3
        if N % 2 == 0:
            for q in range(N//2):
                grid = detonation(r, c, grid)
            return grid
        else:
            for i in range(r):
                for j in range(c):
                    grid[i][j] = "O"
            return grid



rcn = input().split()
r = int(rcn[0])
c = int(rcn[1])
n = int(rcn[2])
grid = []
for _ in range(r):
    grid_item = list(map(str, input()))
    grid.append(grid_item)
result = bomberMan(n, grid, r, c)
for t in result:
    for p in t:
        print(p , end="")
    print("")
