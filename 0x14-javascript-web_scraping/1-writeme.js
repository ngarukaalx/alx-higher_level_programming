#!/usr/bin/node
// writes a string to a file
const fs = require('fs');

// read args from stdin
const args = process.argv.slice(2);

// grab the file path
const filename = args[0];

// grab the string to write
const string = args[1];

// write to file and print the error object if an error occurs
fs.writeFile(filename, string, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
