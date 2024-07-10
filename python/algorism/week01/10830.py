N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


def matrix_multiply(arr1, arr2):
    # print(arr1, arr2)
    arr = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                arr[i][j] += arr1[i][k] * arr2[k][j]
                arr[i][j] %= 1000
    return arr


def dp_fillter(idx):
    if idx == 1:
        return arr
    n_i = idx // 2
    dp_fillter_2 = dp_fillter(n_i)
    return matrix_multiply(
        dp_fillter_2,
        (
            dp_fillter_2
            if idx % 2 == 0
            else matrix_multiply(dp_fillter_2, dp_fillter(1))
        ),
    )


for i in dp_fillter(M):
    print(" ".join(map(str, map(lambda x: x % 1000, i))))
