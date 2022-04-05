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

  // will print with a specific character
  charPrint (c) {
    let sym = c;
    if (sym === undefined) { sym = 'X'; }
    for (let x = 0; x < this.height; x++) {
      console.log(sym.repeat(this.width));
    }
  }
};
