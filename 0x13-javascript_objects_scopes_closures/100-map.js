#!/usr/bin/node

const list = require('./100-data').list;
console.log(list);
const res = list.map((x, y) => x * y);
console.log(res);
