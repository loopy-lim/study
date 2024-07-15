import sys
from collections import deque

input = sys.stdin.readline


K = int(input())


def bfs(start, group):
    q = deque()
    q.append((start, 1))
    group[start] = 1

    while q:
        curr, currGroup = q.popleft()
        for adj in graph[curr]:
            if group[adj] == 0:
                group[adj] = -currGroup
                q.append((adj, -currGroup))
            elif group[adj] == currGroup:
                return False
    return True


for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    group = [0 for _ in range(V + 1)]
    answer = "YES"
    for i in range(1, V + 1):
        if not graph[i]:
            continue
        if group[i] == 0:
            if not bfs(i, group):
                answer = "NO"
                break

    print(answer)
