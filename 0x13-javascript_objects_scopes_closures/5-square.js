#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

//  class Square that defines a square and inherits from Rectangle
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
