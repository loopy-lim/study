N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))


A.sort()


def binary_search(arr, key, l, r):
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        return 1 if arr[0] == key else 2
    if l > r:
        return -1

    m = (l + r) // 2

    if arr[m] == key:
        return m

    elif arr[m] > key:
        r = m - 1
    else:
        l = m + 1

    return binary_search(arr, key, l, r)


for i in B:
    if binary_search(A, i, 0, len(B) - 1) == -1:
        print(0)
    else:
        print(1)
