#!/usr/bin/node
// Will convert argument to integer if it can be converted

const process = require('process');

const val = parseInt(process.argv[2], 10);

if (isNaN(val)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + val);
}
