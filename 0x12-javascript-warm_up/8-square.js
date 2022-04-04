#!/usr/bin/node
// will print a square of specified size

const process = require('process');

const val = parseInt(process.argv[2], 10);

if (isNaN(val)) {
  console.log('Missing size');
} else if (val > 0) {
  for (let x = 0; x < val; x++) {
    console.log('X'.repeat(val));
  }
}
