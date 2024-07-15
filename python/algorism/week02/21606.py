import sys

sys.setrecursionlimit(10**4)

N = int(input())
A = list(map(int, input()))
graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

count = 0

for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

    if A[u - 1] == 1 and A[v - 1] == 1:
        count += 2


def dfs(start):
    visited[start] = True
    inside_count = 0
    for v in graph[start]:
        if A[v - 1] == 1:
            inside_count += 1
        elif not visited[v] and A[v - 1] == 0:
            inside_count += dfs(v)
    return inside_count


for i in range(1, N + 1):
    if A[i - 1] == 0 and not visited[i]:
        result = dfs(i)
        count += result * (result - 1)

print(count)
