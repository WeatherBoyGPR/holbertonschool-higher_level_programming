#!/usr/bin/node

const fs = require('fs');

if (process.argv.length >= 5) {
  const path = [
    process.argv[2],
    process.argv[3],
    process.argv[4]
  ];

  const input1 = fs.readFileSync(path[0], 'utf8');
  const input2 = fs.readFileSync(path[1], 'utf8');

  fs.writeFileSync(path[2], input1 + input2);
}
