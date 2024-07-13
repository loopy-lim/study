class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.parent = value
        self.children = []


N = int(input())
nodes = [Node(i) for i in range(1, N + 1)]

for i in range(N - 1):
    a, b = map(int, input().split())
    nodes[a - 1].children.append(nodes[b - 1])
    nodes[b - 1].children.append(nodes[a - 1])

root_node = nodes[0]


def dfs(node: Node, visited=[]):
    if node.value in visited:
        return
    # print(visited)
    visited.append(node.value)
    for child_node in node.children:
        if child_node.value in visited:
            continue
        child_node.parent = node.value
        dfs(child_node, visited)


dfs(root_node)

# for node in nodes:
#     print(node.value)
#     print(list(map(lambda x: x.value, node.children)))


print("\n".join(map(str, map(lambda x: x.parent, nodes[1:]))))
