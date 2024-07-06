import sys

input = sys.stdin.readline

N = int(input())

row = [0 for _ in range(N)]
result = 0


def check(x, y):
    for i in range(x):
        if row[i] == y or abs(row[i] - y) == x - i:
            return False
    return True


def back_traking(x):
    global result
    if x == N:
        result += 1
        return
    for i in range(N):
        if check(x, i):
            row[x] = i
            back_traking(x + 1)
            row[x] = 0


back_traking(0)
print(result)
