#!/usr/bin/node
const Base = require('./5-square');

class Square extends Base {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    if (c === undefined) {
      for (let i = 0; i < this.size; i++) {
        let row = '';
        for (let j = 0; j < this.size; j++) {
          row += 'X';
        }
        console.log(row);
      }
    } else {
      for (let v = 0; v < this.size; v++) {
        let outPut = '';
        for (let k = 0; k < this.size; k++) {
          outPut += c;
        }
        console.log(outPut);
      }
    }
  }
}
module.exports = Square;
