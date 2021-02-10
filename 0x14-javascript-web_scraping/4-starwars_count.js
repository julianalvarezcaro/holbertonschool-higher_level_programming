#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  error = 0;
  const jsonRep = JSON.parse(body);
  let counter = 0;
  for (film of jsonRep.results) {
    for (character of film.characters) {
      if (character.includes("18")) {
        counter++;
      }
    }
  }
  console.log(counter)
});
