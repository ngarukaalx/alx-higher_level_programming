#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  const newData = args.sort();
  const secondLasgest = newData[newData.length - 2];
  console.log(secondLasgest);
}
