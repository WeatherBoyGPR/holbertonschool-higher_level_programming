#!/usr/bin/node
// Will display the status code of a GET request

const axios = require('axios');

const url = process.argv.slice(2)[0];

axios.get(url)
  .then((response) => {
    console.log('code: %d', response.status);
  })
  .catch((err) => {
    if (err.response) {
      console.log('code: %d', err.response.status);
    }
  });
