from collections import deque

R, C = map(int, input().split())
arr = []

# 사람이 지나갈 수 있는 자리
visited = [[False for _ in range(C)] for _ in range(R)]
q = deque()

# 물이 지나가는 자리
w_visited = [[False for _ in range(C)] for _ in range(R)]
w_q = deque()


for i in range(R):
    arr.append(list(input()))
    for j in range(C):
        if arr[i][j] == "S":
            q.append((i, j))
        elif arr[i][j] == "*":
            w_q.append((i, j))

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def can_move(arr, position, is_S=True):
    global R, C
    result = []
    for x, y in direction:
        x += position[0]
        y += position[1]
        if x >= R or x < 0 or y >= C or y < 0:
            continue
        elif arr[x][y] == "*" or arr[x][y] == "X":
            continue
        elif arr[x][y] == "D":
            if is_S:
                return result, True
            continue
        result.append((x, y))
    return result, False


# 정답
count = 0


def bfs_w(w_visited, w_q, arr):
    new_w_q = deque()
    while w_q:
        i, j = w_q.popleft()
        moves, _ = can_move(arr, (i, j), is_S=False)
        for x, y in moves:
            if w_visited[x][y]:
                continue
            w_visited[i][j] = True
            new_w_q.append((x, y))
            arr[x][y] = "*"
    return new_w_q


def bfs(q, visited, arr):
    new_q = deque()
    while q:
        x, y = q.popleft()
        if w_visited[x][y]:
            continue
        moves, is_finish = can_move(arr, (x, y))
        if is_finish:
            return new_q, is_finish
        for i, j in moves:
            if visited[i][j]:
                continue
            visited[i][j] = True
            new_q.append((i, j))
    return new_q, False


# 결론
count = 0
is_finish = False
while not is_finish and q:
    w_q = bfs_w(w_visited, w_q, arr)
    q, is_finish = bfs(q, visited, arr)
    count += 1
    # print(arr)

if is_finish:
    print(count)
else:
    print("KAKTUS")
