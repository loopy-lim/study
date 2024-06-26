const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [T, P, ...coins] = input.map((i) => i.split(" ").map(Number));
const dp = Array.from({ length: T + 1 }, () => 0);
dp[0] = 1;

for (let i = 0; i < P; i++) {
  const [coin, num] = coins[i];
  for (let j = T; j >= coin; j--) {
    for (let k = 1; k <= num; k++) {
      if (j - coin * k < 0) break;
      dp[j] += dp[j - coin * k];
    }
  }
}

console.log(dp[T]);
