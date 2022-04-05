#!/usr/bin/node
// contains square class

const Rectangle = require('./4-rectangle');

/**
 * Square - represents a square
 * @size: size of square
 */
module.exports = class Square extends Rectangle {
  // constructor
  constructor (size) {
    super(size, size);
  }
};
