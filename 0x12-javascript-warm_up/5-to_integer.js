#!/usr/bin/node

let res = 'Not a number';
const nu = Math.floor(Number(process.argv[2]));

if (nu) {
  res = 'My number: ' + nu;
}

console.log(res);
