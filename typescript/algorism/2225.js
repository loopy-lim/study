const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [N, K] = input[0].split(" ").map(Number);

const A = Array.from({ length: N + 1 }, () => Array(K + 1).fill(1));

for (let i = 1; i <= N; i++) {
  for (let j = 2; j <= K; j++) {
    A[i][j] = (A[i - 1][j] + A[i][j - 1]) % 1_000_000_000;
  }
}

console.log(A[N][K] % 1_000_000_000);
