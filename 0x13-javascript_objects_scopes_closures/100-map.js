#!/usr/bin/node
// imports array from 100-data.js and computes new array

const list = require('./100-data').list;

console.log(list);
console.log(list.map((currentValue, index) => { return currentValue * index; }));
