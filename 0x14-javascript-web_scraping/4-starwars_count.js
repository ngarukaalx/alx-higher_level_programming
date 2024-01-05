#!/usr/bin/node
// script that prints the number of movies where the character “Wedge Antilles” is present

// import request
const request = require('request');

// read command line arguments
const args = process.argv.slice(2);

// grab the url to use
const url = args[0];

// wedge antilles id
const antilles = 18;

// replcae films/ with people/
const modifiedURL = url.replace(/films/, 'people/');
// attach wedge antilles id
const finalURL = `${modifiedURL}${antilles}/`;
// make a Get request
request(finalURL, (error, response, body) => {
  if (error) {
    // output error
    console.error(error);
  }
  const bodyData = JSON.parse(body);
  const films = bodyData.films;
  const numberMovies = films.length;
  console.log(`${numberMovies}`);
});
