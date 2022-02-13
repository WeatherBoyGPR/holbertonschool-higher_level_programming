#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let res = 0;
  for (const i of list) {
    if (i === searchElement) {
      res++;
    }
  }
  return (res);
};
