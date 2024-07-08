N = int(input())
commands = [input().split() for _ in range(N)]

PUSH = "push"
POP = "pop"
SIZE = "size"
EMPTY = "empty"
TOP = "top"

arr = []

for i in commands:
    if i[0] == PUSH:
        arr.append(i[1])
    elif i[0] == POP:
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop())
    elif i[0] == SIZE:
        print(len(arr))
    elif i[0] == EMPTY:
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif i[0] == TOP:
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])
