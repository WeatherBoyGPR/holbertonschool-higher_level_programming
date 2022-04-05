#!/usr/bin/node
// contains Rectangle class

/* Rectangle - represents a rectangle
 * @w: width
 * @h: height
 */
module.exports = class Rectangle {
  // constructor
  constructor (w, h) {
    if (isNaN(parseInt(w, 10)) || isNaN(parseInt(h, 10))) { return; }
    if (w <= 0 || h <= 0) { return; }
    this.width = w;
    this.height = h;
  }

  // prints rectangle
  print () {
    for (let x = 0; x < this.height; x++) {
      console.log('X'.repeat(this.width));
    }
  }

  // swaps values of height and width
  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  // doubles size of rectangle
  double () {
    [this.width, this.height] = [this.width * 2, this.height * 2];
  }
};
