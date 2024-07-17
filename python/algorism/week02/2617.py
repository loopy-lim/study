# 46% 틀림
from collections import deque

N, M = map(int, input().split())
max_arr = [set() for _ in range(N + 1)]
min_arr = [set() for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    max_arr[a].add(b)
    min_arr[b].add(a)

count = 0


def dfs(arr, start):
    global count
    for i in arr[start]:
        if not visited[i]:
            visited[i] = True
            count += 1
            dfs(arr, i)


result = 0
for i in range(1, N + 1):
    visited = [False for _ in range(N + 1)]
    count = 0
    dfs(max_arr, i)
    if count >= (N + 1) // 2:
        result += 1
    count = 0
    dfs(min_arr, i)
    if count >= (N + 1) // 2:
        result += 1
print(result)
