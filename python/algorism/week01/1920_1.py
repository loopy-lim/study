N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))


A.sort()

for i in B:
    try:
        A.index(i)
        print(1)
    except:
        print(0)
