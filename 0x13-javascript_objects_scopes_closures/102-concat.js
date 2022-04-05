#!/usr/bin/node
// will concat file a and file b, stores result in file c

const process = require('process');
const fs = require('fs');

console.log(process.argv[2], process.argv[3], process.argv[4]);

const fileA = fs.readFileSync(process.argv[2]).toString();
const fileB = fs.readFileSync(process.argv[3]).toString();

console.log(fileA + fileB);

fs.writeFile(process.argv[4], fileA + fileB, function (err) {
  if (err) { return console.error(err); }
});
