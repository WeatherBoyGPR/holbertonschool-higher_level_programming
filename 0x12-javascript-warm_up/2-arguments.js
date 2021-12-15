#!/usr/bin/node

let stri = 'No argument';
if (process.argv.length > 2) {
  stri = 'Arguments found';
} else if (process.argv.length === 1) {
  stri = 'Argument found';
}
console.log(stri);
