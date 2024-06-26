#!/usr/bin/node

const Square_1 = require('./5-square');

class Square extends Square_1 {
  charPrint (c) {
    const char = c === undefined ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.widdth));
    }
  }
}
module.exports = Square;
