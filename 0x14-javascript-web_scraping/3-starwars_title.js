#!/usr/bin/node
// Will print the title of a specified Star Wars episode

const axios = require('axios');

const episode = process.argv[2];

axios.get(`https://swapi-api.hbtn.io/api/films/${episode}`)
  .then(res => {
    console.log(res.data.title);
  });
