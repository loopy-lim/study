N = int(input())
M = int(input())

part_counter = [0 for _ in range(N + 1)]
arr = [[] for _ in range(N + 1)]
bigger_arr = [[] for _ in range(N + 1)]
smaller_arr = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y, k = map(int, input().split())
    arr[x].append((y, k))
    bigger_arr[x].append(y)
    smaller_arr[y].append(x)
count_arr = [len(bigger_arr[i]) for i in range(N + 1)]

visited = [False for _ in range(N + 1)]
visited[0] = True


def check_zero(arr):
    global visited
    for i, v in enumerate(arr):
        if visited[i]:
            continue
        if v == 0:
            visited[i] = True
            return i
    return -1


def remove_one(arr, keys):
    for i in keys:
        arr[i] -= 1
    return arr


result = []
while True:
    i = check_zero(count_arr)
    if i == -1:
        break
    result.append(i)
    remove_one(count_arr, smaller_arr[i])

for i in reversed(result):
    for y, k in arr[i]:
        mul = 1 if part_counter[i] == 0 else part_counter[i]
        part_counter[y] += k * mul
    if len(arr[i]) != 0:
        part_counter[i] = 0

for i, v in enumerate(part_counter):
    if v != 0:
        print(f"{i} {v}")
