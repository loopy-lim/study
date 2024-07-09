import sys

import heapq

input = sys.stdin.readline
N = int(input())

q = []

for _ in range(N):
    i = int(input())
    if i == 0:
        if len(q) == 0:
            print(0)
        else:
            print(-heapq.heappop(q))
    else:
        heapq.heappush(q, -i)
