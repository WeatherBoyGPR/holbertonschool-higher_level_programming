#!/usr/bin/node

const dict = require('./101-data').dict;

const res = {};

for (const i in dict) {
  if (res[String(dict[i])] === undefined) {
    res[String(dict[i])] = [i];
  } else {
    res[String(dict[i])].push(i);
  }
}

console.log(res);
