#!/usr/bin/node
// Will print a message depending on number of arguments passed to script

const process = require('process');

const num = process.argv.length - 2;

switch (num) {
  case 0:
    console.log('No argument');
    break;
  case 1:
    console.log('Argument found');
    break;
  default:
    console.log('Arguments found');
    break;
}
