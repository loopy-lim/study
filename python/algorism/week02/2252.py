N, M = map(int, input().split())
bigger_arr = [[] for _ in range(N + 1)]
smaller_arr = [[] for _ in range(N + 1)]
for _ in range(M):
    i, j = map(int, input().split())
    bigger_arr[j].append(i)
    smaller_arr[i].append(j)

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
print(" ".join(map(str, result)))
