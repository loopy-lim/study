from collections import deque

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

minimum = 10**9
is_done = False


def dfs(sums, arr, target, count):
    global minimum, is_done
    if count >= minimum + 1:
        return
    for i in arr:
        if sums + i < target:
            dfs(sums + i, arr, target, count + 1)
        elif sums + i == target:
            minimum = min(minimum, count + 1)
            is_done = True
    return


dfs(0, arr, k, 0)
if is_done:
    print(minimum)
else:
    print(-1)
