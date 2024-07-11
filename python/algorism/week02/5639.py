import sys

sys.setrecursionlimit(10**5)
arr = []

while True:
    try:
        arr.append(int(input()))
    except:
        break

d = {arr[0]: (None, None)}
top = arr[0]


def append_tree(d, key, value):
    # print(d, key, value)
    a = d[key]
    if key > value:
        if not a[0]:
            d[key] = (value, a[1])
            d[value] = (None, None)
        else:
            append_tree(d, a[0], value)
    else:
        if not a[1]:
            d[key] = (a[0], value)
            d[value] = (None, None)
        else:
            append_tree(d, a[1], value)
    # 없는 상태임


def solve3(d, start="A"):
    ds = d.get(start)
    if not ds:
        return False

    if ds[0]:
        if not solve3(d, ds[0]):
            print(ds[0])

    if ds[1]:
        if not solve3(d, ds[1]):
            print(ds[1])

    print(start)
    return True


for i in range(1, len(arr)):
    append_tree(d, top, arr[i])

solve3(d, start=top)
