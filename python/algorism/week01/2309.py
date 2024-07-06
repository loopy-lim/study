arr = [int(input()) for _ in range(9)]

arr.sort()
total = sum(arr)

for i in range(9):
    for j in range(i + 1, 9):
        if total - arr[i] - arr[j] == 100:
            for k in range(9):
                if k == i or k == j:
                    continue
                print(arr[k])
            exit()
