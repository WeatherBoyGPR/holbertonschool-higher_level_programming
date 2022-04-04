#!/usr/bin/node
// Will print two arguments passed to it in the form of a sentence

const process = require('process');

console.log(process.argv[2] + ' is ' + process.argv[3]);
