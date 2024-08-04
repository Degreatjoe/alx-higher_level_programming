#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const characterId = 18;

function countFilmsWithCharacter (url, callback) {
  request(url, (error, response, body) => {
    if (error) {
      return callback(error, null);
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
      countFilmsWithCharacter(data.next, (nextError, nextCount) => {
        if (nextError) {
          return callback(nextError, null);
        }
        callback(null, count + nextCount);
      });
    } else {
      callback(null, count);
    }
  });
}

countFilmsWithCharacter(apiUrl, (error, totalCount) => {
  if (error) {
    console.log(error);
  } else {
    console.log(totalCount);
  }
});
