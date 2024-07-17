import copy
from collections import deque

M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]


def zero_counter(arr):
    count = 0
    for i in arr:
        for j in i:
            for k in j:
                if k == 0:
                    count += 1
    return count


move = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]


def update_arr(arr, q, visited):
    is_changed = False
    result_q = deque()
    while q:
        i, j, k = q.popleft()
        for x, y, z in move:
            if (
                i + x >= H
                or i + x < 0
                or j + y >= N
                or j + y < 0
                or k + z >= M
                or k + z < 0
            ):
                continue
            if visited[i + x][j + y][k + z]:
                continue
            visited[i + x][j + y][k + z] = True
            if arr[i + x][j + y][k + z] == 0:
                arr[i + x][j + y][k + z] = 1
                result_q.append((i + x, j + y, k + z))
                is_changed = True
    return is_changed, result_q


count = 0
is_changed = True
q = deque()
visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]
for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 1:
                q.append((i, j, k))
                visited[i][j][k] = True
while is_changed:
    is_changed, q = update_arr(arr, q, visited)
    count += 1

if zero_counter(arr) == 0:
    print(count - 1)
else:
    print(-1)
