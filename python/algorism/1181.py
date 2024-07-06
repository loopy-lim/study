N = int(input())

arr = [input() for _ in range(N)]

arr = list(set(arr))
arr.sort()
arr.sort(key=len)

print("\n".join(map(str, arr)))
