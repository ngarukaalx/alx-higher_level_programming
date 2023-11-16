#!/usr/bin/node

let numberOfargsPrinted = 0;
exports.logMe = function (item) {
  console.log(`${numberOfargsPrinted}: ${item}`);
  numberOfargsPrinted++;
};
