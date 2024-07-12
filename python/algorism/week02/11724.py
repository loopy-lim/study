N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

parents = [i for i in range(N + 1)]

for a, b in arr:
    ap = parents[a]
    bp = parents[b]

    min_p = ap if ap < bp else bp
    max_p = ap if ap > bp else bp
    parents[a] = min_p
    parents[b] = min_p
    for i in range(N + 1):
        if parents[i] == max_p:
            parents[i] = min_p

# print(parents, list(set(parents)))

print(len(set(parents)) - 1)
