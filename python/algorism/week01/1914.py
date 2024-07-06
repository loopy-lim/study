N = int(input())


def get_move_count(num):
    if num == 1:
        return num
    return get_move_count(num - 1) * 2 + 1


def hanoi(num, l, r):
    if num == 1:
        print(l, r)
        return
    hanoi(num - 1, l, 6 - l - r)
    print(l, r)
    hanoi(num - 1, 6 - l - r, r)


print(get_move_count(N))
if N <= 20:
    hanoi(N, 1, 3)
