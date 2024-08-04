#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const film = JSON.parse(body);
  const characterUrls = film.characters;

  let completedRequests = 0;
  const characters = [];

  characterUrls.forEach(characterUrl => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error(charError);
        return;
      }

      const character = JSON.parse(charBody);
      characters.push(character.name);
      completedRequests++;

      // Print character names after all requests have completed
      if (completedRequests === characterUrls.length) {
        characters.forEach(name => console.log(name));
      }
    });
  });
});
