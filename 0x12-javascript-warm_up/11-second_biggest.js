#!/usr/bin/node
// Will print the second biggest integer in provided arguments

const process = require('process');

if (process.argv.length < 4) {
  console.log(0);
} else {
  let c;
  let a = parseInt(process.argv[3], 10);
  let b = parseInt(process.argv[2], 10);
  if (b > a) {
    [a, b] = [b, a];
  }
  for (let i = 4; i < process.argv.length; i++) {
    c = parseInt(process.argv[i], 10);
    if (c > a) {
      [b, a] = [a, c];
    } else if (c > b) {
      b = c;
    }
  }
  console.log(b);
}
