#!/usr/bin/node

const Request = require('request');
const url = ['https://swapi-api.hbtn.io/api/films/', 'https://swapi-api.hbtn.io/api/people/'];

if (process.argv.length < 3) {
  console.log('invalid number of args');
} else {
  Request(url[0] + process.argv[2], (err, res, body) => {
    if (err) {
      console.log(err);
      return;
    }
    const charlist = JSON.parse(body).characters;
    charprint(charlist, 0);
  });
}

function charprint (idlist, index) {
  Request(idlist[index], (err, res, body) => {
    if (err) {
      console.log(err);
    }
    console.log(JSON.parse(body).name);
    if (index + 1 < idlist.length) {
      charprint(idlist, index + 1);
    }
  });
}
