#!/usr/bin/node

const err = 'Missing size';
const nu = Math.floor(Number(process.argv[2]));
let line = '';

if (nu && !(isNaN(parseInt(nu, 10)))) {
  for (let j = 0; j < nu; j++) {
    line += 'X';
  }
  for (let i = 0; i < nu; i++) {
    console.log(line);
  }
} else {
  console.log(err);
}
