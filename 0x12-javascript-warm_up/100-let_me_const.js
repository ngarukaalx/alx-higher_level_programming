#!/usr/bin/node
global.myVar = 333;
exports.modifies = function () {
  return myVar;
};
