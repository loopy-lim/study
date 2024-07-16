from collections import deque
import heapq

N = int(input())
arr = [list(map(int, list(input()))) for _ in range(N)]
checked = [[float("inf") for _ in range(N)] for _ in range(N)]

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

white_queue = deque()
black_queue = deque()
white_queue.append((0, 0))
count = 0


def bfs_white():
    while white_queue:
        i, j = white_queue.popleft()
        if i == N - 1 and j == N - 1:
            return True
        if checked[i][j] != float("inf"):
            continue
        checked[i][j] = 0
        for x, y in direction:
            if i + x >= N or i + x < 0 or j + y >= N or j + y < 0:
                continue
            if arr[i + x][j + y] == 1:
                white_queue.append((i + x, j + y))
            else:
                black_queue.append((i + x, j + y))
    return False


while not bfs_white():
    white_queue.extend(black_queue)
    count += 1


# print(checked)
print(count)
