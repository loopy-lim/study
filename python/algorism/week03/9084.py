T = int(input())

for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    target_money = int(input())

    dp = [0 for _ in range(10001)]

    for coin in coins:
        dp[coin] += 1
        for i in range(coin, 10001):
            dp[i] += dp[i - coin]

    print(dp[target_money])

    # print(dp)
