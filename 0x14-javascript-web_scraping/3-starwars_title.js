#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';

if (process.argv.length >= 3) {
  const id = process.argv[2];
  request(url + id, (error, response, body) => {
    if (error) console.log(error);
    console.log(JSON.parse(body).title);
  });
}
