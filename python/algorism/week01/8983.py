"""
메모리 초과가 남.
maximum_hunint이 1_000_000_000 이 들어갈 수 있음에 따라
1_000_000_000 * 4 bit, 즉 최대 500메가 바이트를 먹는다.
여기서는 128mb가 조건이었으므로 maximum_hunting을 사용할 수 없고,
정렬 이후 최대한 가까운 위치로 binary로 조사한 뒤에 풀면 된다.
"""

M, N, L = map(int, input().split())

xs = list(map(int, input().split()))
animals = [list(map(int, input().split())) for _ in range(N)]

maximum_hunting = []

result = 0

for x in xs:
    # 없을시 확장
    if x + L > len(maximum_hunting):
        extended_arr = [0 for _ in range((x + L) - len(maximum_hunting))]
        maximum_hunting.extend(extended_arr)

    # 최대 사로 계산
    for i in range(-L, L + 1):
        if x + i < 0 or x + i + 1 > len(maximum_hunting):
            continue
        maximum_hunting[i + x] = max(maximum_hunting[i + x], L - abs(i))
# print(maximum_hunting)
for animal in animals:
    if maximum_hunting[animal[0]] >= animal[1]:
        # print(animal)
        result += 1

print(result)
