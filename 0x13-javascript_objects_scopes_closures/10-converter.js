#!/usr/bin/node
// contains converter function

/**
 * converter - will convert a number from base
 * @base: specified base to convert to
 *
 * Return: converted number
 */
exports.converter = function (base) {
  return function (a) { return a.toString(base); };
};
