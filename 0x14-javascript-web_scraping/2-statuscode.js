#!/usr/bin/node

const request = require('request');

if (process.argv.length >= 3) {
  const url = process.argv[2];

  request(url, (error, response, body) => {
    if (error) console.log(error);
    console.log('code: ' + response.statusCode);
  });
}
