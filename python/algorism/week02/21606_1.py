import sys

sys.setrecursionlimit(10**5)

N = int(input())
A = list(map(int, input()))
graph = [[] for _ in range(N + 1)]
count = 0

for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    if A[u - 1] == 1 and A[v - 1] == 1:
        count += 2


def calc(num):
    return (num - 1) * num


def dfs(key, count, paths=[]):
    global graph, A, first
    if A[key - 1] == 0 and first != key:
        A[key - 1] = -1
        return count
    if key in paths:
        return count
    if A[key - 1] == 1:
        return 1
    paths.append(key)

    for i in graph[key]:
        count += dfs(i, count)
    return count


# print(A)
first = 0
for i in range(len(A)):
    if A[i] == 0:
        first = i + 1
        c = dfs(i + 1, 0)
        if c != 1:
            count += calc(c)
# print(A)
print(count)
