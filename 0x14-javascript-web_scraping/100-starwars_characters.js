#!/usr/bin/node
// prints all characters of a Star Wars movie

// import request
const request = require('request');

// read command line arguments
const args = process.argv.slice(2);

// get first argument which is movie ID
const movieId = args[0];
// url to fetch data
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// make a Get request
request(url, (error, responce, body) => {
  if (error) {
    console.error(error);
  }
  const data = JSON.parse(body);
  const characters = data.characters;

  // loop through data and make a request on each link
  characters.forEach(link => {
    request(link, (error, response, body) => {
      if (error) {
        console.error(error);
      }
      const characterData = JSON.parse(body);
      const characterName = characterData.name;
      console.log(characterName);
    });
  });
});
