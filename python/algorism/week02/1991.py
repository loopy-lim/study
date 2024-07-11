N = int(input())
arr = [input().split() for _ in range(N)]

d = {}
for i in arr:
    if i[1] != ".":
        d[i[0]] = (i[1], None)
    if i[2] != ".":
        if not d.get(i[0]):
            d[i[0]] = (None, i[2])
        else:
            di = d[i[0]]
            d[i[0]] = (di[0], i[2])


def solve1(d, start="A"):
    ds = d.get(start)
    if not ds:
        return False
    print(start, end="")
    if ds[0]:
        if not solve1(d, ds[0]):
            print(ds[0], end="")
    if ds[1]:
        if not solve1(d, ds[1]):
            print(ds[1], end="")
    return True


def solve2(d, start="A"):
    ds = d.get(start)
    if not ds:
        return False

    if ds[0]:
        if not solve2(d, ds[0]):
            print(ds[0], end="")

    print(start, end="")

    if ds[1]:
        if not solve2(d, ds[1]):
            print(ds[1], end="")
    return True


def solve3(d, start="A"):
    ds = d.get(start)
    if not ds:
        return False

    if ds[0]:
        if not solve3(d, ds[0]):
            print(ds[0], end="")

    if ds[1]:
        if not solve3(d, ds[1]):
            print(ds[1], end="")

    print(start, end="")
    return True


solve1(d)
print()
solve2(d)
print()
solve3(d)
print()
