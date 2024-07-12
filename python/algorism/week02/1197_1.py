import sys

sys.setrecursionlimit(10**5)

input = sys.stdin.readline
V, E = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(E)]
arr.sort(key=lambda x: -x[2])

result = 0
parents = [0 for _ in range(V + 1)]
paths = []


def append_parent(a, b):
    if parents[a] == parents[b] and parents[a] != 0:
        return False
    if parents[a] == 0 and parents[b] == 0:
        parents[b] = a
        parents[a] = a
        return True
    if parents[a] == a:
        parents[b] = a
        print(b, a)
        for i in range(V + 1):
            if parents[i] == b:
                parents[i] = b

        return True

    return append_parent(parents[a], b)


def make_mst():
    global result
    if not len(arr):
        return
    a, b, c = arr.pop()
    ain = a in paths
    bin = b in paths
    print([a, b, c], paths, result, parents)
    if bool(ain) ^ bool(bin) or not (ain or bin):
        if not ain:
            paths.append(a)
        if not bin:
            paths.append(b)
        if append_parent(a, b):
            result += c

    make_mst()


make_mst()

print(paths, result, parents)
print(result)
