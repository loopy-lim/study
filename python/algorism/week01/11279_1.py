import sys

sys.setrecursionlimit(10**9)

N = int(input())

arr = []


def pop_reorder(cur_index):
    child_indexs = (cur_index + 1) - 1, (cur_index + 1)
    child_index = child_indexs[0]
    if len(arr) > child_indexs[1]:
        child_index = (
            child_indexs[0]
            if arr[child_indexs[0]] > arr[child_indexs[1]]
            else child_indexs[1]
        )
    if arr[child_index] > arr[cur_index]:
        arr[child_index], arr[cur_index] = arr[cur_index], arr[child_index]
    else:
        return child_index
    return pop_reorder(cur_index)


def pop():
    result = arr.pop(0)
    if len(arr) == 0:
        return result
    arr.insert(0, arr.pop())
    pop_reorder(0)
    return result


def append_reorder(cur_index):
    parrent_index = (cur_index + 1) // 2 - 1
    if arr[parrent_index] < arr[cur_index]:
        arr[parrent_index], arr[cur_index] = arr[cur_index], arr[parrent_index]
    if parrent_index < 1:
        return cur_index
    return append_reorder(cur_index)


def append(key):
    arr.append(key)
    append_reorder(len(arr) - 1)
    return


for _ in range(N):
    i = int(input())
    if i == 0:
        if len(arr) == 0:
            print(0)
        else:
            result = pop()
            print(result)
    else:
        append(i)
    # print(arr)
