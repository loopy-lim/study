import sys
import heapq

input = sys.stdin.readline

N = int(input())

arr = []

for _ in range(N):
    h, o = map(int, input().split())
    if o > h:
        arr.append((h, o))
    else:
        arr.append((o, h))

arr.sort()
arr.sort(key=lambda x: x[1])

d = int(input())

result = 1 if arr[0][1] - arr[0][0] <= d else 0
clac_arr = []

h, o = arr.pop(0)
clac_arr.append((h, o))
h_c, o_c = arr.pop(0)

while len(arr):
    while len(arr):
        print(arr, clac_arr)
        if h_c >= h and o_c <= h + d:
            clac_arr.append((h_c, o_c))
            h_c, o_c = arr.pop(0)
            print(1111, arr, clac_arr)
            continue
        if o_c <= o and h_c >= o - d:
            clac_arr.append((h_c, o_c))
            h_c, o_c = arr.pop(0)
            print(2222, arr, clac_arr)
            continue
        break

    result = max(result, len(clac_arr))
    if len(clac_arr):
        h, o = clac_arr[0]
    if len(arr):
        h_c, o_c = arr.pop(0)

print(result)
