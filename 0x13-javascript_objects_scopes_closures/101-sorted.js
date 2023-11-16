#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};

for (const [userId, occurence] of Object.entries(dict)) {
  if (newDict[occurence]) {
    newDict[occurence].push(userId);
  } else {
    newDict[occurence] = [userId];
  }
}
console.log(newDict);
