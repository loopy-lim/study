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
result = 0

print("## init arr:", arr)

clac_arr = []


def solve(cur_position):
    while len(arr):
        h, o = heapq.heappop(arr)
        if o - h > d:
            continue
        if len(clac_arr) == 0:
            clac_arr.append((h, o))
            continue
        result = max(
            len(
                list(
                    filter(
                        lambda x: x[0] >= cur_position and x[1] <= cur_position + d,
                        clac_arr,
                    )
                )
            ),
            result,
        )
