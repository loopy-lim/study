N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

trable = [False for _ in range(N)]
result = 10_000_001


def dfs(cur, weight, deps, start):
    global trable, result

    if deps == N:
        if W[cur][start] != 0:
            result = min(result, weight + W[cur][start])
        return
    for i in range(N):
        if not trable[i] and W[cur][i] != 0:
            trable[i] = True
            dfs(i, weight + W[cur][i], deps + 1, start)
            trable[i] = False


for i in range(N):
    trable[i] = True
    dfs(i, 0, 1, i)
    trable[i] = False

print(result)
