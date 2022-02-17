#!/usr/bin/node

const Request = require('request');

if (process.argv.length >= 3) {
  const url = process.argv[2];
  const test = 'https://swapi-api.hbtn.io/api/people/18/';
  let num = 0;

  Request(url, (error, response, body) => {
    if (error) return;
    const res = JSON.parse(body).results;
    for (const i in res) {
      for (const l in res[i].characters) {
        if (res[i].characters[l] === test) {
          num += 1;
          break;
        }
      }
    }
    console.log(num);
  });
}
