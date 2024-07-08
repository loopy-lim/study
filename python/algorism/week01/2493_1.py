import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

result = [0 for _ in range(N)]


def block_index(arr, x):
    for i in range(x - 1, -1, -1):
        if arr[i] >= arr[x]:
            return i + 1
    return 0


for i in range(N - 1, -1, -1):
    result[i] = block_index(arr, i)


print(" ".join(map(str, result)))
