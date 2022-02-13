#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    let line = '';
    let x = this.width;
    let y = this.height;

    while (x) {
      line = line + c;
      x--;
    }

    while (y) {
      console.log(line);
      y--;
    }
  }
};
