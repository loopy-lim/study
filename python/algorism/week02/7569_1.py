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


def update_arr(arr):
    is_changed = False
    q = deque()
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if arr[i][j][k] == 1:
                    q.append((i, j, k))
    visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]
    while q:
        if visited[i][j][k]:
            continue
        visited[i][j][k] = True
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
                is_changed = True
    return is_changed


count = 0
is_changed = True
while is_changed:
    is_changed = update_arr(arr)
    count += 1

if zero_counter(arr) == 0:
    print(count - 1)
else:
    print(-1)
