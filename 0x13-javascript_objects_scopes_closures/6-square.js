#!/usr/bin/node

const SquareOld = require('./5-square');

const square = class Square extends SquareOld {
  charPrint (c = 'X') {
    let w;
    let h;
    for (h = 0; h < this.height; h++) {
      for (w = 0; w < this.width; w++) {
        process.stdout.write(c);
      }
      console.log();
    }
  }
};
module.exports = square;
