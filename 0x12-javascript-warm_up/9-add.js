#!/usr/bin/node
// Will print the sum of two arguments

const process = require('process');

console.log(parseInt(process.argv[2], 10) + parseInt(process.argv[3], 10));
