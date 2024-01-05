#!/usr/bin/node
// script that prints the title of a Star Wars movie where the episode number
// matches a given integer.

// import request
const request = require('request');

// read command line arguments
const args = process.argv.slice(2);

// grab movie id
const movieId = args[0];

// url to use
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
// make a get request
request(url, (error, response, body) => {
  // check errors
  if (error) {
    // skip
  }
  // parse the json resppnse
  const movieData = JSON.parse(body);

  console.log(movieData.title);
});
