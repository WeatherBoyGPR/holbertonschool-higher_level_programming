#!/usr/bin/node
// Will write a string to a file

const fs = require('fs');

const args = process.argv.slice(2, 4);

fs.writeFile(args[0], args[1], function (err, data) {
  if (err) {
    console.log(err);
  }
});
