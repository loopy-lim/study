import sys
import heapq

n = int(input())
left = []
right = []

for i in range(n):
    x = int(sys.stdin.readline())

    if len(left) == 0 or -left[0] >= x:
        heapq.heappush(left, -x)
    else:
        heapq.heappush(right, x)

    if len(left) > len(right) + 1:
        temp = -heapq.heappop(left)
        heapq.heappush(right, temp)

    elif len(right) > len(left):
        temp = heapq.heappop(right)
        heapq.heappush(left, -temp)

    print(-left[0])
