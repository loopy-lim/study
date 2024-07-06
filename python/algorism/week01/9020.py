T = int(input())


def prime_list(n):
    sieve = [True] * n

    m = int(n**0.5)

    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(i * 2, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i]]


prime_numbers = prime_list(10000)


def is_prime(arr, key):
    try:
        arr.index(key)
        return True
    except:
        return False


for i in range(T):
    n = int(input())
    l, r = int(n / 2), int(n / 2)

    while not is_prime(prime_numbers, l) or not is_prime(prime_numbers, r):
        l -= 1
        r += 1
    print(l, r)
