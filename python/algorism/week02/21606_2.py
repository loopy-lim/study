import sys

sys.setrecursionlimit(10**4)

N = int(input())
A = input()
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


count = 0
start = 0


def dfs(graph, key, paths):
    global count, start
    paths.append(key)
    for node in graph[key]:
        if node in paths:
            continue
        # print(paths, node, [A[node - 1]])
        if A[node - 1] == "1":
            count += 1
            continue
        # if start != key and A[node - 1] == "1":
        #     return
        dfs(graph, node, paths)


for i in range(N):
    if A[i] == "1":
        start = i + 1
        dfs(graph, i + 1, [])
        # print(i + 1, count)
print(count)
