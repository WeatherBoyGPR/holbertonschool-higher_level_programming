#!/usr/bin/node
// will read and print the content of a file

const fs = require('fs');

const filename = process.argv.slice(2)[0];

fs.readFile(filename, function (err, data) {
  if (err) {
    console.log(err);
  }
  console.log(data.toString());
});
