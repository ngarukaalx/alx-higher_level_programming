#!/usr/bin/node
const Base = require('./5-square');

class Square extends Base {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.size; i++) {
        let row = '';
        for (let j = 0; j < this.size; j++) {
          row += 'c';
        }
        console.log(row);
      }
    } else {
      for (let s = 0; s < this.size; s++) {
        let outPut = '';
        for (let v = 0; v < this.size; v++) {
          outPut += 'X';
        }
        console.log(outPut);
      }
    }
  }
}

module.exports = Square;
