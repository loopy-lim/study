import sys

sys.setrecursionlimit(10**5)

input = sys.stdin.readline
V, E = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(E)]
arr.sort(key=lambda x: -x[2])

result = 0
parents = [i for i in range(V + 1)]


def renew_parents(a, b):
    if parents[a] != parents[b]:
        smm = a if parents[a] < parents[b] else b
        mxx = a if parents[a] > parents[b] else b
        max_v = parents[mxx]
        parents[mxx] = parents[smm]
        # 재 정렬
        for i in range(1, V + 1):
            if parents[i] == max_v:
                renew_parents(i, smm)
        return True
    return False


def mst():
    global result
    # 다 조사
    if not len(arr):
        return
    a, b, c = arr.pop()
    # print("###", parents, a, b, c, result)
    # 이미 간 곳이라고 하면 조사하지 않기
    # 부모가 같다면 정렬하지 않기
    if renew_parents(a, b):
        result += c

    mst()


mst()
print(result)
