import heapq as hq
import sys

input = sys.stdin.readline

N = int(input())


arr1 = []
arr2 = []

for _ in range(N):
    i = int(input())
    if len(arr1) == 0:
        arr1.append(-i)
    else:
        if -arr1[0] > i:
            hq.heappush(arr1, -i)
        else:
            hq.heappush(arr2, i)

    # print(arr1, arr2)

    if len(arr1) == len(arr2) and len(arr1) > 0 and len(arr2) > 0:
        print(-arr1[0] if -arr1[0] < arr2[0] else arr2[0])
    else:
        gap = len(arr1) - len(arr2)
        if gap > 0:
            print(-arr1[0])
            if abs(gap) >= 2:
                hq.heappush(arr2, -hq.heappop(arr1))
        else:
            print(arr2[0])
            if abs(gap) >= 2:
                hq.heappush(arr1, -hq.heappop(arr2))
