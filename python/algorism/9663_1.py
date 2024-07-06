'''
n Queen문제라면 어떻게 해결해야 할까?
1. 퀸은 한 행에 하나씩만 놓일 수 있다.
2. 퀸은 한 열에 하나씩만 놓일 수 있다.
3. 퀸은 대각선 방향으로도 이동할 수 있다.
'''

n = int(input())

row = [[0 for _ in range(n)]  for _ in range(n)]
result = 0

def check(x, y):
    for i in range(n):
        if row[i][y] == 1:
            return False
    for i in range(x):
        if y - (x - i) >= 0 and row[i][y - (x - i)] == 1:
            return False
        if y + (x - i) < n and row[i][y + (x - i)] == 1:
            return False
    return True

def dfs(x):
    global result
    if x == n:
        result += 1
        return
    for i in range(n):
        if check(x, i):
            row[x][i] = 1
            dfs(x + 1)
            row[x][i] = 0

dfs(0)
print(result)