import sys
import heapq

input = sys.stdin.readline

N = int(input())

arr = []

for _ in range(N):
    h, o = map(int, input().split())
    if o > h:
        heapq.heappush(arr, (h, o))
    else:
        heapq.heappush(arr, (o, h))


d = int(input())

end_arr = []
result = 0

while len(arr):
    h, o = heapq.heappop(arr)
    if d >= o - h:
        heapq.heappush(end_arr, (d + h, o))
    if len(end_arr) != 0:
        last_end_arr_value = end_arr[0]
        while last_end_arr_value[0] < h:
            last_end_arr_value = heapq.heappop(end_arr)
    result = max(len(list(filter(lambda x: x[0] >= o and x[1] <= o, end_arr))), result)
    # print(end_arr, h, o, d)

print(result)
