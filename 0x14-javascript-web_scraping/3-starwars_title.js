#!/usr/bin/node

const request = require('request');
const epi = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${epi}`;

request(url, function (error, response, body) {
  error = 0;
  const jsonRep = JSON.parse(body);
  console.log(jsonRep.title);
});
