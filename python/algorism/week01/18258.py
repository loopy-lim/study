from collections import deque

N = int(input())
commands = [input().split() for _ in range(N)]

PUSH = "push"
POP = "pop"
SIZE = "size"
EMPTY = "empty"
FRONT = "front"
BACK = "back"

arr = deque([])

for i in commands:
    if i[0] == PUSH:
        arr.append(i[1])
    elif i[0] == POP:
        print(arr.popleft() if len(arr) != 0 else -1)
    elif i[0] == SIZE:
        print(len(arr))
    elif i[0] == EMPTY:
        print(0 if len(arr) != 0 else 1)
    elif i[0] == FRONT:
        print(arr[0] if len(arr) != 0 else -1)
    elif i[0] == BACK:
        print(arr[-1] if len(arr) != 0 else -1)
