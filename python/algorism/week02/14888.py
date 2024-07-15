N = int(input())
arr = list(map(int, input().split()))
sign = ["+", "-", "*", "/"]
calc = []
for i, v in enumerate(map(int, input().split())):
    calc.extend([sign[i]] * v)

minium = 10**9 + 1
maximum = -(10**9) - 1


def dfs(result, deps=1, path=[]):
    global N, minium, maximum
    if deps == N:
        # print(path, result)
        minium = min(minium, result)
        maximum = max(maximum, result)
        return
    for i in range(len(calc)):
        if i in path:
            continue
        path.append(i)
        tmp_result = result
        if calc[i] == "+":
            tmp_result = result + arr[deps]
        elif calc[i] == "-":
            tmp_result = result - arr[deps]
        elif calc[i] == "*":
            tmp_result = result * arr[deps]
        elif calc[i] == "/":
            if result < 0:
                tmp_result = -(-result // arr[deps])
            else:
                tmp_result = result // arr[deps]
        dfs(tmp_result, deps + 1, path)
        path.pop()


dfs(arr[0])
print(maximum)
print(minium)
