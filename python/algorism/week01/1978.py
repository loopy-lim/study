_ = input()

arr = map(int, input().split())
prime_numbers = []

for i in range(2, 1000):
    is_prime = True
    for j in range(2, i):
        if (i % j) == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(i)

result = 0
for i in arr:
    try:
        prime_numbers.index(i)
        result += 1
    except:
        pass

print(result)
