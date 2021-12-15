#!/usr/bin/node

let stri = 'No argument';
if (process.argv.length > 1) {
  stri = 'Arguments found';
}
console.log(stri);
