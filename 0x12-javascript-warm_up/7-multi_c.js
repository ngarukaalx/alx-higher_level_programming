#!/usr/bin/node

const args = process.argv.slice(2);
const intValue = parseInt(args[0]);

if (isNaN(intValue)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < intValue; i++) {
    console.log('C is fun');
  }
}
