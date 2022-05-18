#!/usr/bin/node
// Will display the status code of a GET request

const axios = require('axios');

const url = process.argv.slice(2)[0];

axios(url)
  .then(function (response) {
    console.log(response.status);
  });
