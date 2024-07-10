import sys

input = sys.stdin.readline

N = int(input())

arr = []

for _ in range(N):
    h, o = map(int, input().split())
    if o > h:
        arr.append((h, o))
    else:
        arr.append((o, h))

arr.sort(key=lambda x: x[1])
arr.sort(key=lambda x: x[0])

d = int(input())
arr = list(filter(lambda x: x[1] - x[0] <= d, arr))
result = 0

for i in range(len(arr)):
    cur_h = arr[i][0]
    # print(list(filter(lambda x: x[1] <= cur_h + d and x[0] >= cur_h, arr)))
    result = max(
        len(list(filter(lambda x: x[1] <= cur_h + d and x[0] >= cur_h, arr))), result
    )

# print(arr)

print(result)
