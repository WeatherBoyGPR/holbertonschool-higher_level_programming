#!/usr/bin/node
// contains Rectangle class

/* Rectangle - represents a rectangle
 * @w: width
 * @h: height
 */
module.exports = class Rectangle {
  constructor (w, h) {
    if (isNaN(parseInt(w, 10)) || isNaN(parseInt(h, 10))) { return; }
    if (w <= 0 || h <= 0) { return; }
    this.width = w;
    this.height = h;
  }
};
