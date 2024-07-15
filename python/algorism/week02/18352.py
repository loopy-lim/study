import collections

N, M, K, X = map(int, input().split())
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)


def bfs(K, X, arr):
    q = collections.deque()
    q.append([X, 0])
    result = []
    visited = []
    while q:
        start, deps = q.popleft()
        if start in visited:
            continue
        visited.append(start)
        if deps == K:
            result.append(start)
            continue
        for i in arr[start]:
            q.append([i, deps + 1])
    return result


result = sorted(bfs(K, X, arr))
if len(result):
    print("\n".join(map(str, result)))
else:
    print(-1)
