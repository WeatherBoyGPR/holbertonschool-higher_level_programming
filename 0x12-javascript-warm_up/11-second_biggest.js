#!/usr/bin/node

let res = 0;
let gre;

if (process.argv.length > 3) {
  gre = Number(process.argv[2]);
  res = gre;
  for (const key in process.argv) {
    if (gre < Number(process.argv[key])) {
      gre = Number(process.argv[key]);
    } else if (res < Number(process.argv[key])) {
      res = Number(process.argv[key]);
    }
  }
}
console.log(res);
