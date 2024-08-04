#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const characterId = 18;

function countFilmsWithCharacter (url, callback) {
  request(url, (error, response, body) => {
    if (error) {
      console.log(error);
      return;
    }

    const data = JSON.parse(body);
    let count = 0;

    data.results.forEach(film => {
      if (film.characters.some(char => char.endsWith(`/${characterId}/`))) {
        count++;
      }
    });

    // If there is a next page, recurse to handle pagination
    if (data.next) {
      countFilmsWithCharacter(data.next, (nextCount) => {
        callback(count + nextCount);
      });
    } else {
      callback(count);
    }
  });
}

countFilmsWithCharacter(apiUrl, (totalCount) => {
  console.log(totalCount);
});
