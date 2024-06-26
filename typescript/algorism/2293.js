const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, k] = input[0].split(" ").map(Number);
const coins = input
  .slice(1)
  .map(Number)
  .sort((a, b) => b - a);

const getMinus = (k, coin) => {
  let tryCount = 0;
  while (k >= 0) {
    k -= coin;
    tryCount += 1;
  }
  return [k + coin, tryCount];
};

const solution = (k, coinsIndex, result) => {
  [k, tryCount] = getMinus(k, coins[coinsIndex]);
  console.log(k, coins[coinsIndex]);

  if (coinsIndex >= coins.length - 1) {
    return result;
  }
  if (k === 0) {
    result += 1;
  }
  if (k > 0) {
    return solution(k, coinsIndex + 1, result);
  }
  k += tryCount * coins[coinsIndex];
  return solution(k, coinsIndex + 1, result);
};

console.log(solution(k, 0, 1));
