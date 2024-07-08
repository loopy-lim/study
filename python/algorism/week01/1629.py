A, B, C = map(int, input().split())

binary_b = f"{B:b}"[::-1]
dp = [0 for i in range(len(binary_b))]

dp[0] = A % C
for i in range(len(dp)):
    if dp[i] == 0:
        dp[i] = (dp[i - 1] ** 2) % C

result_arr = [dp[i] for i in range(len(dp)) if binary_b[i] == "1"]

# print(dp, binary_b, result_arr)

multis = 1
for i in result_arr:
    multis *= i
print(multis % C)
