N = int(input())

arr = [int(input()) for _ in range(N)]


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left, equal, right = [], [], []
    for i in arr:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            equal.append(i)
    return quick_sort(left) + equal + quick_sort(right)


print("\n".join(map(str, arr)))
