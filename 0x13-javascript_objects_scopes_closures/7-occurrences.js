#!/usr/bin/node
// contains nbOccurences function

exports.nbOccurences = function (list, searchElement) {
  let res = 0;

  for (let i = 0; i < list.length; i++) { res += (list[i] === searchElement); }
  return res;
};
