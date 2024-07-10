N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[] * N for _ in range(M + 1)]


def matrix_multiply(arr1, arr2):
    # print(arr1, arr2)
    arr = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                arr[i][j] += arr1[i][k] * arr2[k][j]
                arr[i][j] %= 1000
    return arr


dp[1] = arr


def dp_fillter(idx):
    if len(dp[idx]) != 0:
        return dp[idx]
    for i in range(idx, -1, -1):
        if len(dp[i]) == 0:
            n_i = i // 2
            if i % 2 == 0:
                dp[i] = matrix_multiply(dp_fillter(n_i), dp_fillter(n_i))
                return dp[i]
            else:
                dp[i] = matrix_multiply(
                    matrix_multiply(dp_fillter(n_i), dp_fillter(n_i)), dp_fillter(1)
                )
                return dp[i]


dp_fillter(M)
# print(dp)
for i in dp[-1]:
    print(" ".join(map(str, i)))
