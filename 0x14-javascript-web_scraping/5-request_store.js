#!/usr/bin/node
/*
 * Obtains contents of webpage and stores it in a file
 * arg 1 - webpage
 * arg 2 - filepath to store response
 */

const Request = require('request');
const Fs = require('fs');

if (process.argv.length < 4) {
  console.log('invalid number of args');
} else {
  Request(process.argv[2], (error, response, body) => {
    if (error) {
      console.log(error);
      return;
    }

    Fs.writeFile(process.argv[3], body, (err) => {
      if (err) console.log(err);
    });
  });
}
