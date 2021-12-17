#!/usr/bin/node

let gre;
let res = 0;
const len = process.argv.length;

if (len > 3) {
  gre = process.argv[2];
  res = gre;

  for (let i = 3; i < len; i++) {
    if (Number(process.argv[i]) > gre) {
      gre = Number(process.argv[i]);
    }
  }
  for (let i = 3; i < len; i++) {
    if (Number(process.argv[i]) < gre && Number(process.argv[i]) > res) {
      res = Number(process.argv[i]);
    }
  }
}
console.log(res);
