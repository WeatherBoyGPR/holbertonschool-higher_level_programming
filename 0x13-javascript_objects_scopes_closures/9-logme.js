#!/usr/bin/node

let logMeVar = 0;
exports.logMe = function (item) {
  console.log(logMeVar + ': ' + item);
  logMeVar++;
};
