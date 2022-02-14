#!/usr/bin/node

exports.converter = function (base) {
  return function (res) { res.toString(base); };
};
