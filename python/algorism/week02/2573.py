# 31% 메모리 초과

import sys
import copy

sys.setrecursionlimit(10**5)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def calc_round(arr, i, j):
    return len(list(filter(lambda x: x, [arr[i + x][j + y] <= 0 for x, y in moves])))


def make_boolean(arr):
    return [[i > 0 for i in j] for j in arr]


def first_ice(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j]:
                return i, j
    return -1, -1


def remove_icebug(arr, i, j):
    if arr[i][j]:
        arr[i][j] = False
        for x, y in moves:
            remove_icebug(arr, i + x, j + y)


result = 1
# calc_icebug(arr)
while True:
    prev_arr = copy.deepcopy(arr)
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 0:
                continue
            arr[i][j] = max(0, arr[i][j] - calc_round(prev_arr, i, j))

    boolean_arr = make_boolean(arr)
    i, j = first_ice(boolean_arr)
    if i == -1 and j == -1:
        break
    remove_icebug(boolean_arr, i, j)
    i, j = first_ice(boolean_arr)
    if not (i == -1 and j == -1):
        break
    result += 1


if first_ice(arr) == (-1, -1):
    print(0)
else:
    print(result)
