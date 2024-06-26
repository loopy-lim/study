const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

class MinimumHeap {
  constructor() {
    this.arr = [];
  }
  pop() {
    if (this.arr.length === 0) {
      return 0;
    }
    if (this.arr.length === 1) {
      return this.arr.pop();
    }
    const result = this.arr[0];
    this.arr[0] = this.arr.pop();
    let idx = 0;
    while (idx < this.arr.length) {
      const leftIdx = idx * 2 + 1;
      const rightIdx = idx * 2 + 2;
      let minIdx = idx;
      if (leftIdx < this.arr.length && this.arr[leftIdx] < this.arr[minIdx]) {
        minIdx = leftIdx;
      }
      if (rightIdx < this.arr.length && this.arr[rightIdx] < this.arr[minIdx]) {
        minIdx = rightIdx;
      }
      if (minIdx === idx) {
        break;
      }
      const temp = this.arr[idx];
      this.arr[idx] = this.arr[minIdx];
      this.arr[minIdx] = temp;
      idx = minIdx;
    }
    return result;
  }
  push(num) {
    this.arr.push(num);
    let idx = this.arr.length - 1;
    while (idx > 0) {
      const parentIdx = Math.floor((idx - 1) / 2);
      if (this.arr[idx] < this.arr[parentIdx]) {
        const temp = this.arr[idx];
        this.arr[idx] = this.arr[parentIdx];
        this.arr[parentIdx] = temp;
        idx = parentIdx;
      } else {
        break;
      }
    }
  }
}

const heap = new MinimumHeap();
const N = Number(input[0]);
for (let i = 1; i <= N; i++) {
  const num = Number(input[i]);
  if (num === 0) {
    console.log(heap.pop());
  } else {
    heap.push(num);
  }
}
