#!/usr/bin/node

const Request = require('request');

if (process.argv.length >= 3) {
  const url = process.argv[2];
  let num = 0;

  Request(url, (error, response, body) => {
    if (error) return;
    const res = JSON.parse(body).results;
    for (const i in res) {
      const cList = res[i].characters;
      for (const c in cList) {
        if (cList[c].includes('18')) {
          num += 1;
        }
      }
    }
    console.log(num);
  });
}
