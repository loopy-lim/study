N = int(input())

for i in range(N):
    R, S = input().split()
    R = int(R)
    for j in S:
        print(j * R, end="")
    print()
