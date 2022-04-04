#!/usr/bin/node
// will print C is fun a specified number of times

const process = require('process');

const val = parseInt(process.argv[2], 10);

if (isNaN(val)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < val; i++) {
    console.log('C is fun');
  }
}
