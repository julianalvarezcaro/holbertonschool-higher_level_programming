#!/usr/bin/node

const myClass = class Rectangle {
  constructor (width, height) {
    if (width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }

  print () {
    let h;
    let w;
    for (h = 0; h < this.height; h++) {
      for (w = 0; w < this.width; w++) {
        process.stdout.write('x');
      }
      console.log();
    }
  }
};
module.exports = myClass;
