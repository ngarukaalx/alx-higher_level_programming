#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  for (const item of list) {
    if (searchElement === item) {
      i += 1;
    }
  }
  return i;
};
