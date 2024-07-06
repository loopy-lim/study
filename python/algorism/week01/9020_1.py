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


def get_approach_prime_index(arr, num):
    for i in range(len(arr)):
        if arr[i] > num:
            return i - 1
    return -1


for i in range(T):
    n = int(input())
    result = [0, 10000]
    for j in range(get_approach_prime_index(prime_numbers, n)):
        for k in range(len(prime_numbers) - j):
            if prime_numbers[j] + prime_numbers[k] > n:
                break
            if prime_numbers[k] + prime_numbers[j] == n:
                if result[1] - result[0] > prime_numbers[j] - prime_numbers[k]:
                    result = [prime_numbers[j], prime_numbers[k]]

    print(" ".join(map(str, result)))
