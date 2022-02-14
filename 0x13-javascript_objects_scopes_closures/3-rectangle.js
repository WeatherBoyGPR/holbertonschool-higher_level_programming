#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && typeof h === 'number') {
      if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
      }
    }
  }

  print () {
    let line = '';
    let x = this.width;
    let y = this.height;

    while (x) {
      line = line + 'X';
      x--;
    }

    while (y) {
      console.log(line);
      y--;
    }
  }
};