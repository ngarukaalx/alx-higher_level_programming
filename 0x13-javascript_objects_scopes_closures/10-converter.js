#!/usr/bin/node

exports.converter = function (base) {
  return function convert (number) {
    if (number < base) {
      return number.toString(base);
    } else {
      return convert(Math.floor(number / base)) + (number % base).toString(base);
    }
  };
};
