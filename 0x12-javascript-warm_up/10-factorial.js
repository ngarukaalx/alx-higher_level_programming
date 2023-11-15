#!/usr/bin/node

function factorial(a) {
  if (a === 0) {
    return 1;
  } else {
      return a * factorial(a - 1);
  }
}

const args = process.argv.slice(2);
if (args.length == 0) {
  console.log(1);
}
console.log(factorial(parseInt(args[0])));
