#!/usr/bin/node
// contains logMe function

let logMeCount = 0;
/**
 * logMe - will print arguments with arguments already printed
 */
exports.logMe = function (item) {
  console.log(logMeCount + ': ' + item);
  logMeCount += 1;
};
