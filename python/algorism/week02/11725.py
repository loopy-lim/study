import sys

sys.setrecursionlimit(10**5)

N = int(input())
nodes = {}


def node_put(nodes, a, b):
    node = nodes.get(a)
    if node:
        node.append(b)
    else:
        nodes[a] = [b]


for _ in range(N - 1):
    a, b = map(int, input().split())
    node_put(nodes, a, b)
    node_put(nodes, b, a)

result = [0 for _ in range(N + 1)]


def dfs(result, nodes: dict, key):
    # print(result, key)
    node = nodes.get(key)
    for i in node:
        if result[i]:
            continue
        result[i] = key
        dfs(result, nodes, i)


dfs(result, nodes, 1)
print("\n".join(map(str, result[2:])))
