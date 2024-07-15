from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(N)]

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(arr):
    q = deque()
    q.append([0, 0, 1])
    while q:
        # print(q)
        i, j, deps = q.popleft()
        if i == N - 1 and j == M - 1:
            return deps
        for x, y in direction:
            x += i
            y += j
            if x >= N or x < 0 or y >= M or y < 0 or arr[x][y] == 0:
                continue
            arr[x][y] = 0  # 방문위치
            q.append([x, y, deps + 1])


print(bfs(arr))
