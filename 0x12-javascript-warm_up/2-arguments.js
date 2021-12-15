#!/usr/bin/node

const count = process.argv.length;
let stri = 'No argument';
if (count === 3) {
  stri = 'Argument found';
} else if (count > 3) {
  stri = 'Arguments found';
}
console.log(stri);
