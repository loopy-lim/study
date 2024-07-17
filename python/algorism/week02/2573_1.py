import copy
import sys

sys.setrecursionlimit(10**5)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


def draw_boolean(arr):
    return [[True if arr[j][i] else False for i in range(M)] for j in range(N)]


moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def count_around(i, j):
    global before_arr
    if i >= N or i < 0 or j >= M or j < 0:
        return False
    return before_arr[i][j] <= 0


def update_arr(i, j, arr):
    if arr[i][j] == 0:
        return
    # print(list(filter(lambda x: x, [count_around(i + x, j + y) for x, y in moves])))
    arr[i][j] = max(
        arr[i][j]
        - len(
            list(filter(lambda x: x, [count_around(i + x, j + y) for x, y in moves]))
        ),
        0,
    )


def check_split_iceberg(i, j, arr, paths):
    if i >= N or i < 0 or j >= M or j < 0:
        return
    if arr[i][j] and not str((i, j)) in paths:
        # print(i, j, arr[i][j])
        arr[i][j] = False
        paths.append(str((i, j)))
        for x, y in moves:
            check_split_iceberg(i + x, j + y, arr, paths)


def get_first_false(arr):
    for i, a1 in enumerate(arr):
        for j, a2 in enumerate(a1):
            if a2:
                return i, j
    return -1, -1


max_iceberg = max(max(*arr))
count = 0

while max_iceberg:
    before_arr = copy.deepcopy(arr[:])
    for i in range(N):
        for j in range(M):
            update_arr(i, j, arr)
    max_iceberg = max(max(*arr))
    count += 1

    boolean_arr = draw_boolean(arr)
    x, y = get_first_false(boolean_arr)
    if x == -1 and y == -1:
        # print("### 1번째")
        # print("\n".join(map(str, (draw_boolean(arr)))))
        break
    check_split_iceberg(x, y, boolean_arr, [])
    # print("\n".join(map(str, boolean_arr)), x, y)
    x, y = get_first_false(boolean_arr)
    if not x == -1 or not y == -1:
        # print("### 2번째")
        # print("\n".join(map(str, (draw_boolean(arr)))))
        break

print(count)
