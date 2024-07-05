N = int(input())


def get_factorial(n):
    if n == 0:
        return 1
    return n * get_factorial(n - 1)


print(get_factorial(N))
