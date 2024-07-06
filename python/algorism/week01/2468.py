import sys

sys.setrecursionlimit(10**9)

N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]


# 잠기면 False, 안잠기면 True
def draw_map(deps, arr):
    return [list(map(lambda x: False if x <= deps else True, arr2)) for arr2 in arr]


def draw_map_false(arr, x, y):
    if arr[x][y]:
        arr[x][y] = False
    if y + 1 < len(arr):
        if arr[x][y + 1]:
            draw_map_false(arr, x, y + 1)
    if x + 1 < len(arr):
        if arr[x + 1][y]:
            draw_map_false(arr, x + 1, y)
    if y - 1 > 0:
        if arr[x][y - 1]:
            draw_map_false(arr, x, y - 1)
    if x - 1 > 0:
        if arr[x - 1][y]:
            draw_map_false(arr, x - 1, y)


def get_count_field(arr, count, x, y):
    if arr[x][y]:
        count += 1
        draw_map_false(arr, x, y)
    if x + 1 < len(arr):
        return get_count_field(arr, count, x + 1, y)
    if y + 1 < len(arr):
        return get_count_field(arr, count, 0, y + 1)
    if x + 1 == len(arr) and y + 1 == len(arr):
        return count


max_count = 1
for i in range(100):
    maps = draw_map(i, M)
    max_count = max(get_count_field(maps, 0, 0, 0), max_count)

print(max_count)
