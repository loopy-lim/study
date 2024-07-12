N, M, V = map(int, input().split())
arr = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)


def dfs(key, paths=[]):
    paths.append(key)
    if len(paths) == N:
        return paths
    for i in arr[key]:
        if not i in paths:
            paths = dfs(i, paths)
    return paths


def bfs(key):
    paths = []
    nexts = [key]
    while len(nexts):
        next = nexts.pop(0)
        for i in arr[next]:
            if not i in paths:
                nexts.append(i)
        if not next in paths:
            paths.append(next)
    return paths


for i in range(N + 1):
    arr[i].sort()

# print(arr)
print(" ".join(map(str, dfs(V))))
print(" ".join(map(str, bfs(V))))
