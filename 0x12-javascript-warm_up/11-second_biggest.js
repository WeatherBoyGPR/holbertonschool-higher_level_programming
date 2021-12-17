#!/usr/bin/node

let gre;
let res = 0;
const len = process.argv.length;

if (len > 3) {
  if (process.argv[2] >= process.argv[3]) {
    gre = process.argv[2];
    res = process.argv[3];
  } else {
    gre = process.argv[3];
    res = process.argv[2];
  }

  for (let i = 4; i < len; i++) {
    if (process.argv[i] > gre) {
      res = gre;
      gre = process.argv[i];
    }
  }
}
console.log(res);
