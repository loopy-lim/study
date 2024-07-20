import sys

input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
dp = [[0] * (N + 1) for _ in range(N + 1)]

arr = []
a, b = map(int, input().split())
arr.append(a)
arr.append(b)
for i in range(1, N):
    a, b = map(int, input().split())
    arr.append(b)

for i in range(1, N + 1):
    dp[i][i] = 0  # 초깃값 셋팅 (i=j인 경우들)

for j in range(1, N + 1):
    for i in range(j - 1, 0, -1):
        min_value = INF
        for k in range(i, j):
            min_value = min(
                min_value, dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
            )
        dp[i][j] = min_value

print(dp[1][N])
