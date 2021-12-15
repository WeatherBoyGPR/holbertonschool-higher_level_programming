#!/usr/bin/node

let right;
let left;

if (process.argv[2]) {
  left = process.argv[2];
}
if (process.argv[3]) {
  right = process.argv[3];
}

console.log(left + ' is ' + right);
