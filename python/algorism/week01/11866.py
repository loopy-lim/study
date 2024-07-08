N, K = map(int, input().split())

arr = [i for i in range(1, N + 1)]
result = []

while len(arr) != 0:
    for i in range(K - 1):
        arr.append(arr.pop(0))
    result.append(arr.pop(0))


print("<", end="")
print(", ".join(list(map(str, result))), end="")
print(">")
