#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  const newData = args.map(Number).sort((a, b) => b - a);
  const secondLasgest = newData[1];
  console.log(secondLasgest);
}
