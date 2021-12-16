#!/usr/bin/node

const err = 'Missing number of occurrences';
const nu = Math.floor(Number(process.argv[2]));

if (nu) {
  for (let i = 0; i < nu; i++) {
    console.log('C is fun');
  }
} else {
  console.log(err);
}
