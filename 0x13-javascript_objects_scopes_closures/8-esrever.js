#!/usr/bin/node

exports.esrever = function (list) {
  let newList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    newList += list[i];
  }
  return newList;
};
