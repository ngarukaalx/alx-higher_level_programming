#!/usr/bin/node

const args = process.argv.slice(2);
const args1 = args[0];

const intValue = parseInt(args1);

if (isNaN(intValue)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + `${intValue}`);
}
