#!/usr/bin/node
// prints the status code of a get request
const request = require('request');

// get args
const args = process.argv.slice(2);

// grab url
const url = args[0];

// make a get request
request(url, (error, response, body) => {
	console.log('code:', response.statusCode);
});
