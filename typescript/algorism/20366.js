const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const N = Number(input[0]);
const H = input[1].split(" ").map(Number);

let max = [Infinity, 0, 0, 0, 0];
