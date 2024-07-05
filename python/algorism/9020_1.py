T = int(input())


prime_numbers = []

for i in range(2, 1000):
    is_prime = True
    for j in range(2, i):
        if (i % j) == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(i)


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
