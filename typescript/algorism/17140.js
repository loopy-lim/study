const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [r, c, k] = input[0].split(" ").map(Number);
let arr = input.slice(1).map((i) => i.split(" ").map(Number));
let arrayType = "R";
const MAX_TIME = 100;
const MAX_ARRAY_LENGTH = 100;

const isFinish = (arr) =>
  arrayType === "C" ? arr[r - 1][c - 1] === k : arr[c - 1][r - 1] === k;
const switchArryType = () => (arrayType = arrayType === "R" ? "R" : "C");

const ordering = (arr) =>
  arr.map((a) =>
    Array.from(
      a.sort().reduce((acc, cur) => {
        if (cur === 0) return acc;
        if (acc.has(cur)) {
          acc.set(cur, acc.get(cur) + 1);
        } else {
          acc.set(cur, 1);
        }
        return acc;
      }, new Map())
    )
      .sort((a, b) => a[1] - b[1])
      .flat()
  );

const reordering = (arr) => {
  const maxLength = Math.min(
    arr.reduce((acc, cur) => Math.max(acc, cur.length), 0),
    MAX_ARRAY_LENGTH
  );

  arr = arr.map((i) => {
    const originLength = i.length;
    i.length = maxLength;
    return i.fill(0, originLength, maxLength);
  });
  if ((arr, arr.length >= maxLength)) return arr;
  switchArryType();
  return arr.reduce(
    (acc, cur) => cur.map((_, i) => [...(acc[i] || []), cur[i]]),
    []
  );
};

const result = (time = 0) => {
  if (isFinish(arr)) return time;
  if (time === MAX_TIME) return -1;
  arr = reordering(ordering(arr));
  return result(time + 1);
};

console.log(result());
