N, M = list(map(int, input().split()))
woods = list(map(int, input().split()))

woods.sort()
woods.reverse()


def get_wooks_sums(arr, cut_height):
    sum_arr = []
    for i in arr:
        if i > cut_height:
            sum_arr.append(i - cut_height)
    return sum(sum_arr)


result = 0
last_result = -1
r = woods[0]
l = 0
m = 0
while True:
    if result == last_result:
        break
    m = (l + r) // 2
    last_result = result
    result = get_wooks_sums(woods, m)
    if result < M:
        r = m - 1
    elif result > M:
        l = m + 1

print(m)
