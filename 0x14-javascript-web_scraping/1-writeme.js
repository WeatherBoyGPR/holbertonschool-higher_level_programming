#!/usr/bin/node

const fs = require('fs');

if (process.argv.length >= 4) {
  fs.writeFile(process.argv[2], process.argv[3], 'utf8', function (err, data) {
    if (err) {
      console.log(err);
    }
  });
}
