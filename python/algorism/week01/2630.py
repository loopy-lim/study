N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

P1 = 0
P2 = 0


def dfs(arr, x, y, w):
    global P1, P2
    color = arr[x][y]
    bw = w // 2
    for i in range(x, x + w):
        for j in range(y, y + w):
            if color != arr[i][j]:
                dfs(arr, x, y, bw)
                dfs(arr, x + bw, y, bw)
                dfs(arr, x, y + bw, bw)
                dfs(arr, x + bw, y + bw, bw)
                return
    if color == 1:
        P1 += 1
    else:
        P2 += 1


dfs(arr, 0, 0, N)

print(P2)
print(P1)
