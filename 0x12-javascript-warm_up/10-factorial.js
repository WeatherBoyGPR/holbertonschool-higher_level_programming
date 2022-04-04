#!/usr/bin/node
// Will compute and print factorial of integer

const process = require('process');

/*
 * factorialFunc - will calculate the factorial of val
 *
 * @val: single integer
 * Return: factorial of val
 */
function factorialFunc (val) {
  if (val) {
    return (val * factorialFunc(val - 1));
  }
  return (1);
}

const val = parseInt(process.argv[2], 10);

if (isNaN(val)) {
  console.log(1);
} else {
  console.log(factorialFunc(val));
}
