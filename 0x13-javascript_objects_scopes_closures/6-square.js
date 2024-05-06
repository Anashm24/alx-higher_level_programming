#!/usr/bin/node
// a square and inherits from Square
const SquareS = require('./5-square.js');

class Square extends SquareS {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
