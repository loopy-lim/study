N = int(input())

arr = [int(input()) for _ in range(N)]


def counting_sort(arr):
    max_num = max(arr)
    min_num = min(arr)
    counting_arr = [0] * (max_num - min_num + 1)
    for i in arr:
        counting_arr[i - min_num] += 1
    result = []
    for i in range(len(counting_arr)):
        result += [i + min_num] * counting_arr[i]
    return result


print("\n".join(map(str, counting_sort(arr))))
