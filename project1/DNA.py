n = int(input())
genes = list(map(str, input().rstrip().split()))
health = list(map(int, input().rstrip().split()))
s = int(input())
A = []
for i in range(s):
    firstLastd = input().split()
    first = int(firstLastd[0])
    last = int(firstLastd[1])
    d = firstLastd[2]
    value = 0

    useful_genes = genes[first:last + 1]
    for i in range(len(useful_genes)):
        x = len(useful_genes[i])
        for j in range(0, len(d) - x + 1):
            if d[j:j + x] == useful_genes[i]:
                value += health[i + first]
    A.append(value)

print(min(A), max(A))

