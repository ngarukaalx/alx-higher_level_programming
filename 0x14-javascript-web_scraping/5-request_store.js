#!/usr/bin/node
// gets the contents of a webpage and stores it in a file
const fs = require('fs');
const request = require('request');

// read args from stdin
const args = process.argv.slice(2);

// grab the file path and url
const filename = args[1];
const url = args[0];

// make a Get request
request(url, (error, response, body) => {
  if (error) {
    // print error
    console.log(error);
  }
  const data = (body);
  // write to file and print the error object if an error occurs
  fs.writeFile(filename, data, 'utf-8', (err) => {
    if (err) {
      console.err(err);
    }
  });
});
