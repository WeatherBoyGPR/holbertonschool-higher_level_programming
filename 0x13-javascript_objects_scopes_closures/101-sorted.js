#!/usr/bin/node
// will import a dictory and compute dictionary of user ids by occurrence

const dict = require('./101-data').dict;
console.log(dict);

const res = {};

for (const [key, value] of Object.entries(dict)) {
  if (res[value] === undefined) { res[value] = [key]; } else {
    res[value].push(key);
  }
}

console.log(res);
