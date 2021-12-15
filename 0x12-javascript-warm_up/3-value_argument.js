#!/usr/bin/node

let res = 'No argument';
if (process.argv[2]) {
  res = process.argv[2];
}
console.log(res);
