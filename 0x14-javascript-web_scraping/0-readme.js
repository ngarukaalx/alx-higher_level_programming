#!/usr/bin/node
// reads and prints the content of a file

const fs = require('fs');

// reads command line arguments
const args = process.argv.slice(2);

// grab filename
const filename = args[0];

// read the content of the file and print error if file does not exits
fs.readFile(filename, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }

  console.log(`${data}`);
});
